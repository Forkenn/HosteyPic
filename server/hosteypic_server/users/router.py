import asyncio

import sqlalchemy as alch

from typing import List
from concurrent.futures import ThreadPoolExecutor

from fastapi import UploadFile, APIRouter, status, Response, Depends
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.database import get_async_session
from hosteypic_server.exceptions import (
    FileTypeException, FIleParamsException, AlreadyExistException, YourselfException,
    BannedException
)
from hosteypic_server.image import ImageManager
from hosteypic_server.users.tools import get_object_by_id
from hosteypic_server.users.models import User
from hosteypic_server.likes.models import Like
from hosteypic_server.users.schemas import (
    SUserReadSingle, SMultiUserRead, SUserEdit, SUserReadFull, SUserUsernameEdit
)
from hosteypic_server.posts.models import Post
from hosteypic_server.posts.schemas import SPostsPreviews, SPostPreview

router = APIRouter(prefix='/users', tags=['Users'])

responses = {
    404: {"description": "Item not found"},
    400: {"description": "Bad params or no access rights"},
    204: {"description": "Successful Response"}
}

current_optional_user = fastapi_users.current_user(optional=True, active=True)
current_user = fastapi_users.current_user(active=True)
current_verified_user = fastapi_users.current_user(active=True, verified=True)
current_moderator = RoleManager(is_moderator=True)
current_superuser = fastapi_users.current_user(superuser=True)

@router.get('/')
async def get_users(
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> SMultiUserRead:
    query = alch.select(User).order_by(User.id.asc()).slice(start, end)
    users = (await session.execute(query)).scalars().all()

    return {'count': len(users), 'items': users}

@router.get('/current')
async def get_current_user(user: User = Depends(current_user)) -> SUserReadFull:
    return user

@router.get('/{user_id}', responses=responses)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_optional_user)
) -> SUserReadSingle:
    user_resp: User = await get_object_by_id(user_id, session)
    response = SUserReadSingle(**user_resp.__dict__)                # TODO: fix stupid code
    response.is_following = None

    if user:
        response.is_following = await user.is_following(user_resp)

    response.followers_count = await user_resp.followers_count()
    return response

@router.delete('/{user_id}', responses=responses)
async def delete_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    query = alch.delete(User).where(User.id == user_id)
    await session.execute(query)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/current', responses=responses)
async def edit_current_user(
        data: SUserEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_verified_user)
):
    await user.update(**data.model_dump())
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{user_id}', responses=responses)
async def edit_user_by_id(
        user_id: int,
        data: SUserEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):  
    user_resp: User = await get_object_by_id(user_id, session)

    await user_resp.update(**data.model_dump())
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/current/avatar', responses=responses)
async def set_avatar(
    image: UploadFile,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_verified_user)
):
    if image.content_type not in ('image/jpeg', 'image/png'):
        raise FileTypeException()
    
    current_loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        filename = await current_loop.run_in_executor(
            pool, ImageManager.upload_avatar, image.file
        )

    if not filename:
        raise FIleParamsException()
    
    user.avatar = filename
    await session.commit()

    return {'avatar': filename}

@router.patch('/current/username', responses=responses)
async def change_username(
        new_username: SUserUsernameEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = alch.select(User).where(User.username == new_username.username)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise AlreadyExistException()
    
    user.username = new_username.username
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{user_id}/username', responses=responses)
async def change_username_by_id(
        user_id: int,
        new_username: SUserUsernameEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    query = alch.select(User).where(User.username == new_username.username)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise AlreadyExistException()
    
    user_check.username = new_username.username
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/ban', responses=responses)
async def ban_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    user_resp: User = await get_object_by_id(user_id, session)
    user_resp.is_active = False
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/unban', responses=responses)
async def unban_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    user_resp: User = await get_object_by_id(user_id, session)
    user_resp.is_active = True
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/moder', responses=responses)
async def user_to_moderator_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    user_resp: User = await get_object_by_id(user_id, session)
    user_resp.is_moderator = True
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/unmoder', responses=responses)
async def moderator_to_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    user_resp: User = await get_object_by_id(user_id, session)
    user_resp.is_moderator = False
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/follow', responses=responses)
async def follow_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_verified_user)
):
    if user_id == user.id:
        raise YourselfException()

    follow_user: User = await get_object_by_id(user_id, session)
    if not follow_user.is_active:
        raise BannedException()

    await user.follow(follow_user)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/unfollow', responses=responses)
async def unfollow_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_verified_user)
):
    if user_id == user.id:
        raise YourselfException()

    unfollow_user: User = await get_object_by_id(user_id, session)
    await user.unfollow(unfollow_user)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/{user_id}/posts/liked')
async def get_user_liked_posts(
        user_id: int,
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostsPreviews:
    query = alch.select(Like).where(
        Like.user_id == user_id
    ).slice(start, end).options(selectinload(Like.post))

    likes_obj_list = (await session.execute(query)).scalars().all()
    response_list = []
    for like in likes_obj_list:
        response = SPostPreview(**like.post.__dict__)
        if user:
            response.is_deletable = await like.post.deletable_flag(user)
            response.is_editable = await like.post.editable_flag(user)

        response_list.append(response)

    response_list.reverse()     #TODO: temporary solution
    return {'count': len(response_list), 'items': response_list}

@router.get('/{user_id}/posts')
async def get_user_posts_by_id(
        user_id: int,
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
) -> SPostsPreviews:
    user_resp: User = await get_object_by_id(user_id, session)
    query = user_resp.posts.select().order_by(
        Post.timestamp.desc()
    ).slice(start, end)

    posts = (await session.execute(query)).scalars().all()

    if not user:
        return {'count': len(posts), 'items': posts}
    
    response_list = []
    for post in posts:
        response = SPostPreview(**post.__dict__)
        response.is_deletable = await post.deletable_flag(user)
        response.is_editable = await post.editable_flag(user)

        response_list.append(response)

    response_list.reverse()     #TODO: temporary solution
    return {'count': len(response_list), 'items': response_list}