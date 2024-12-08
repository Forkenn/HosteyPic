import sqlalchemy as alch

from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.exceptions import NotFoundException, NotAllowedException
from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post
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
