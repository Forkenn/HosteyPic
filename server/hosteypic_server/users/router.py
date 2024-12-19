import asyncio

import sqlalchemy as alch

from concurrent.futures import ThreadPoolExecutor

from fastapi import UploadFile, APIRouter, status, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.database import get_async_session
from hosteypic_server.exceptions import (
    FileTypeException, FIleParamsException, AlreadyExistException, YourselfException,
    BannedException, NotFoundException, NotAllowedException
)
from hosteypic_server.image import ImageManager
from hosteypic_server.auth.schemas import SUsername
from hosteypic_server.users.models import User
from hosteypic_server.users.schemas import (
    SUserReadSingle, SMultiUserRead, SUserEdit, SUserReadFull
)

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

@router.get('')
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
    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

    response = SUserReadSingle(**user_resp.__dict__)
    response.is_following = None
    if user:
        response.is_following = await user.is_following(user_resp)

    response.followers_count = await user_resp.followers_count()
    return response

@router.get('/search/{username}', responses=responses)
async def search_user_by_name(
    username: str,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser)
) -> SUserReadSingle:
    query = alch.select(User).where(User.username == username)
    user_resp = (await session.execute(query)).scalar()

    if not user_resp:
        raise NotFoundException()

    response = SUserReadSingle(**user_resp.__dict__)
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
    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

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
        new_username: SUsername,
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
        new_username: SUsername,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    query = alch.select(User).where(User.username == new_username.username)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise AlreadyExistException()
    
    user_resp = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()
    
    user_resp.username = new_username.username
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/ban', responses=responses)
async def ban_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()
    
    if user_resp.is_moderator and not user.is_superuser:
        raise NotAllowedException()

    user_resp.is_active = False
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/unban', responses=responses)
async def unban_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

    if user_resp.is_moderator and not user.is_superuser:
        raise NotAllowedException()

    user_resp.is_active = True
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/moder', responses=responses)
async def user_to_moderator_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

    user_resp.is_moderator = True
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/{user_id}/unmoder', responses=responses)
async def moderator_to_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

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

    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

    if not user_resp.is_active:
        raise BannedException()

    await user.follow(user_resp)
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

    user_resp: User = await session.get(User, user_id)
    if not user_resp:
        raise NotFoundException()

    await user.unfollow(user_resp)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
