import asyncio
from concurrent.futures import ThreadPoolExecutor

from fastapi import (
    UploadFile, APIRouter, HTTPException, status, Response, Depends
)

import sqlalchemy as alch
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.database import get_async_session
from hosteypic_server.image import ImageManager
from hosteypic_server.users.dao import change_user, change_fields
from hosteypic_server.users.models import User
from hosteypic_server.users.schemas import (
    SUserReadSingle, SMultiUserRead, SUserEdit, SUserReadFull, SUserUsernameEdit
)

router = APIRouter(prefix='/users', tags=['Users'])

responses ={
    404: {"description": "Item not found"},
    400: {"description": "Bad params or no access rights"},
    204: {"description": "Successful Response"}
}

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
    user: User = Depends(current_user)
) -> SUserReadSingle:
    query = alch.select(User).where(User.id == user_id)
    user_resp = (await session.execute(query)).scalar()
    if not user_resp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  detail="ITEM_NOT_FOUND"
        )

    response = SUserReadSingle(**user_resp.__dict__)                # TODO: fix stupid code
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
        user: User = Depends(current_verified_user)
):
    await change_user(user.id, data)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{user_id}', responses=responses)
async def edit_user_by_id(
        user_id: int,
        data: SUserEdit,
        user: User = Depends(current_moderator)
):
    await change_user(user_id, data)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/avatar/{user_id}', responses=responses)
async def get_avatar_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    query = alch.select(User).where(User.id == user_id)
    user_resp = (await session.execute(query)).scalar()
    if not user_resp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  detail="ITEM_NOT_FOUND"
        )
    
    return {'avatar': user_resp.avatar}

@router.post('/avatar', responses=responses)
async def set_avatar(
    image: UploadFile,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_verified_user)
):
    if image.content_type not in ('image/jpeg', 'image/png'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="INVALID_FILE_TYPE"
        )
    
    current_loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        filename = await current_loop.run_in_executor(
            pool, ImageManager.upload_avatar, image.file
        )

    if not filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="WRONG_IMAGE_PARAMS"
        )
    
    user.avatar = filename
    await session.commit()

    return {'avatar': filename}

@router.patch('/username/current', responses=responses)
async def change_username(
        new_username: SUserUsernameEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = alch.select(User).where(User.username == new_username.username)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="USERNAME_ALREADY_TAKEN"
        )
    
    await change_user(user.id, new_username)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/username/{user_id}', responses=responses)
async def change_username_by_id(
        user_id: int,
        new_username: SUserUsernameEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    query = alch.select(User).where(User.username == new_username.username)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="USERNAME_ALREADY_TAKEN"
        )
    
    await change_user(user_id, new_username)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/ban/{user_id}', responses=responses)
async def ban_user_by_id(
        user_id: int,
        user: User = Depends(current_moderator)
):
    await change_fields(user_id, {'is_active': False})

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/unban/{user_id}', responses=responses)
async def unban_user_by_id(
        user_id: int,
        user: User = Depends(current_moderator)
):
    await change_fields(user_id, {'is_active': True})

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/moder/{user_id}', responses=responses)
async def user_to_moderator_by_id(
        user_id: int,
        user: User = Depends(current_moderator)
):
    await change_fields(user_id, {'is_moderator': True})

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/unmoder/{user_id}', responses=responses)
async def moderator_to_user_by_id(
        user_id: int,
        user: User = Depends(current_moderator)
):
    await change_fields(user_id, {'is_moderator': False})

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/follow/{user_id}', responses=responses)
async def follow_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_verified_user)
):
    if user_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CAN_NOT_FOLLOW_YOURSELF"
        )

    follow_user: User = await session.scalar(
        alch.select(User).where(User.id == user_id)
    )

    if follow_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="USER_NOT_FOUND"
        )
    
    if not follow_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CAN_NOT_FOLLOW_BANNED"
        )

    await user.follow(follow_user)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/unfollow/{user_id}', responses=responses)
async def unfollow_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_verified_user)
):
    if user_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CAN_NOT_UNFOLLOW_YOURSELF"
        )

    unfollow_user: User = await session.scalar(
        alch.select(User).where(User.id == user_id)
    )

    if unfollow_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="USER_NOT_FOUND"
        )

    await user.unfollow(unfollow_user)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/is-following/{user_id}', responses=responses)
async def check_following_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    follow_user: User = await session.scalar(
        alch.select(User).where(User.id == user_id)
    )

    if follow_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="USER_NOT_FOUND"
        )

    response = await user.is_following(follow_user)

    return {'is_following': response}

@router.get('/followers-count/{user_id}', responses=responses)
async def get_followed_count_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    check_user = await session.scalar(
        alch.select(User).where(User.id == user_id)
    )

    if check_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="USER_NOT_FOUND"
        )

    response = await check_user.followers_count()

    return {'followers': response}
