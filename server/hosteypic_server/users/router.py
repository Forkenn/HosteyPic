from fastapi import APIRouter, HTTPException, status, Response, Depends
from fastapi_users.password import PasswordHelper

import sqlalchemy as alch
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.database import get_async_session
from hosteypic_server.users.dao import change_user
from hosteypic_server.users.models import User
from hosteypic_server.users.schemas import (
    SUserRead, SMultiUserRead, SUserEdit, SUserReadFull, SUserEmailEdit,
    SUserUsernameEdit, SUserActiveSet, SUserModeratorSet
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
) -> SUserRead:
    query = alch.select(User).where(User.id == user_id)
    response = (await session.execute(query)).scalar()
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  detail="ITEM_NOT_FOUND"
        )

    return response

@router.delete('/current', responses=responses)
async def delete_current_user(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    await session.delete(user)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

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

@router.patch('/edit/current', responses=responses)
async def edit_current_user(
        data: SUserEdit,
        user: User = Depends(current_user)
):
    await change_user(user.id, data)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/edit/{user_id}', responses=responses)
async def edit_user_by_id(
        user_id: int,
        data: SUserEdit,
        user: User = Depends(current_moderator)
):
    await change_user(user_id, data)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/change_username/current', responses=responses)
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

@router.patch('/change_username/{user_id}', responses=responses)
async def change_username_by_id(
        user_id: int,
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
    
    await change_user(user_id, new_username)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/change_email/current', responses=responses)
async def change_email(
        new_email: SUserEmailEdit,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = alch.select(User).where(User.email == new_email.email)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EMAIL_ALREADY_TAKEN"
        )
    
    await change_user(user.id, new_email)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/change_password/current', responses=responses)
async def change_password(
        old: str,
        new: str,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    password_helper = PasswordHelper()

    if not password_helper.verify_and_update(old, user.hashed_password)[0]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="LOGIN_BAD_CREDENTIALS"
        )
    
    query = alch.update(User).values(
        hashed_password=password_helper.hash(new)
    ).where(User.id == user.id)

    await session.execute(query)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/active/{user_id}', responses=responses)
async def edit_active_by_id(
        user_id: int,
        data: SUserActiveSet,
        user: User = Depends(current_moderator)
):
    await change_user(user_id, data)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/moderator/{user_id}', responses=responses)
async def edit_moderator_by_id(
        user_id: int,
        data: SUserModeratorSet,
        user: User = Depends(current_superuser)
):
    await change_user(user_id, data)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
