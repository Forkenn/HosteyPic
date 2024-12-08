import asyncio

import sqlalchemy as alch
import sqlalchemy.orm as orm

from concurrent.futures import ThreadPoolExecutor

from fastapi import APIRouter, UploadFile, status, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import func

from hosteypic_server.database import get_async_session
from hosteypic_server.image import ImageManager
from hosteypic_server.auth.manager import fastapi_users
from hosteypic_server.users.models import User
from hosteypic_server.tags.models import Tag
from hosteypic_server.posts.models import Post
from hosteypic_server.likes.models import Like
from hosteypic_server.posts.schemas import (
    SPostRead, SPostsPreviews, SPostCreate, SPostEdit
)
from hosteypic_server.posts.tools import get_validate_post, get_post_previews
from hosteypic_server.exceptions import (
    FileTypeException, FIleParamsException, NotFoundException
)

router = APIRouter(prefix='/posts', tags=['Posts'])

current_optional_user = fastapi_users.current_user(optional=True)
current_user = fastapi_users.current_user(active=True, verified=True)

@router.get('')
async def get_last_posts(
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostsPreviews:
    Author = orm.aliased(User)
    query = (
        alch.select(Post)
        .join(Post.author.of_type(Author))
        .where(
            Author.is_active == True
        )
        .group_by(Post)
        .order_by(Post.timestamp.desc())
        .slice(start, end)
    )
    posts = (await session.execute(query)).scalars().all()

    if not user:
        return {'count': len(posts), 'items': posts}
    
    response_list = await get_post_previews(user, posts)
    return {'count': len(response_list), 'items': response_list}

@router.get('/followed')
async def get_followed_posts(
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> SPostsPreviews:
    Author = orm.aliased(User)
    Follower = orm.aliased(User)

    query = (
        alch.select(Post)
        .join(Post.author.of_type(Author))
        .join(Author.followers.of_type(Follower), isouter=True)
        .where(alch.and_(Follower.id == user.id, Author.id != user.id))
        .group_by(Post)
        .order_by(Post.timestamp.desc())
        .slice(start, end)
    )

    posts = (await session.execute(query)).scalars().all()
    response_list = []

    response_list = await get_post_previews(user, posts)
    return {'count': len(response_list), 'items': response_list}

@router.get('/search')
async def search_last_posts(
        q: str,
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostsPreviews:
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

    if not user:
        return {'count': len(posts), 'items': posts}
    
    response_list = await get_post_previews(user, posts)
    return {'count': len(response_list), 'items': response_list}

@router.get('/followed/search')
async def search_followed_posts(
        q: str,
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> SPostsPreviews:
    pass

@router.get('/{post_id}')
async def get_post_by_id(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostRead:
    query = (
        alch.select(Post)
        .where(Post.id == post_id)
        .options(selectinload(Post.tags))
    )
    post = (await session.execute(query)).scalar()

    if not post:
        raise NotFoundException()
    
    response = SPostRead(**post.__dict__)
    if user:
        response.is_deletable = await post.deletable_flag(user)
        response.is_editable = await post.editable_flag(user)
        response.is_liked = await post.liked_flag(user)

    response.tags_list = post.tags

    return response

@router.post('')
async def create_post(
        attachment: UploadFile,
        post_data: SPostCreate = Depends(),
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    if attachment.content_type not in ('image/jpeg', 'image/png'):
        raise FileTypeException()
    
    current_loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        filename = await current_loop.run_in_executor(
            pool, ImageManager.upload_attachment, attachment.file
        )

    if not filename:
        raise FIleParamsException()
    
    post_dict = post_data.__dict__
    tags_ids = post_dict.pop("tag")
    post_dict.update({'user_id': user.id, 'attachment': filename})

    tags_list = []
    if tags_ids:
        query = alch.select(Tag).where(Tag.id.in_(tags_ids))
        tags_list = (await session.execute(query)).scalars().all()

    new_post = Post(**post_dict)
    if tags_list:
        new_post.tags = tags_list

    session.add(new_post)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{post_id}')
async def edit_post_by_id(
        post_id: int,
        post_data: SPostEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    post: Post = await get_validate_post(session, user, post_id)
    new_post_data = post_data.__dict__
    new_tags_ids: list[int] = new_post_data.pop("tag")
    await session.refresh(post, attribute_names=["tags"])

    tags_list = []
    if new_tags_ids:
        query = alch.select(Tag).where(Tag.id.in_(new_tags_ids))
        tags_list = (await session.execute(query)).scalars().all()

    post.tags = tags_list
    await post.update(**new_post_data)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/{post_id}')
async def delete_post_by_id(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    post: Post = await get_validate_post(session, user, post_id)
    await session.delete(post)
    await session.commit()                   # flush didn't work

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/users/{user_id}')
async def get_user_posts_by_id(
        user_id: int,
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostsPreviews:
    user_resp: User = await session.get(User, user_id)
    query = user_resp.posts.select().order_by(
        Post.timestamp.desc()
    ).slice(start, end)

    posts = (await session.execute(query)).scalars().all()
    if not user:
        return {'count': len(posts), 'items': posts}
    
    response_list = await get_post_previews(user, posts)
    return {'count': len(response_list), 'items': response_list}

@router.get('/users/{user_id}/liked')
async def get_user_liked_posts(
        user_id: int,
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostsPreviews:
    query = (
        alch.select(Like)
        .where(Like.user_id == user_id)
        .slice(start, end)
        .options(selectinload(Like.post))
    )

    likes_obj_list = (await session.execute(query)).scalars().all()
    posts = [like.post for like in likes_obj_list]
    if not user:
        return {'count': len(posts), 'items': posts}

    response_list = await get_post_previews(user, posts)
    return {'count': len(response_list), 'items': response_list}
