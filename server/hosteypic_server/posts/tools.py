import sqlalchemy as alch

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import func

from hosteypic_server.exceptions import NotFoundException, NotAllowedException
from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post
from hosteypic_server.tags.models import Tag
from hosteypic_server.posts.schemas import SPostPreview

async def get_validate_post(session: AsyncSession, user: User, post_id: int) -> Post:
    query = alch.select(Post).where(Post.id == post_id)
    post: Post = (await session.execute(query)).scalar()

    if not post:
        raise NotFoundException()
    if post.user_id != user.id and not user.is_moderator:
        raise NotAllowedException()
    
    return post

async def get_post_previews(user: User, posts: list[Post]) -> SPostPreview:
    response_list = []
    for post in posts:
        response = SPostPreview(**post.__dict__)
        response.is_deletable = await post.deletable_flag(user)
        response.is_editable = await post.editable_flag(user)
        response.is_liked = await post.liked_flag(user)

        response_list.append(response)

    return response_list

async def get_posts_by_query(
        start: int,
        end: int,
        q: str,
        session: AsyncSession
):
    query = (
        alch.select(Post)
        .where(
            func.to_tsvector(
                Post.lang,
                func.coalesce(Post.title, '')
                .concat(' ')
                .concat(func.coalesce(Post.body, ''))
            )
            .bool_op("@@")(func.plainto_tsquery(q))
        ).slice(start, end)
    )
    posts = (await session.execute(query)).scalars().all()
    return posts

async def get_posts_by_tags(
        start: int,
        end: int,
        tags_names: list[str],
        session: AsyncSession
) -> list[Post]:
    query = (
        alch.select(Post)
        .join(Post.tags)
        .where(Tag.name.in_(tags_names))
        .distinct()
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.timestamp.desc())
        .slice(start, end)
    )

    posts = (await session.execute(query)).scalars().all()
    return posts
