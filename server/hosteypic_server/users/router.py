from typing import List

from fastapi import APIRouter, HTTPException, status, Response, Depends

import sqlalchemy as alch
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.database import get_async_session
from hosteypic_server.users.models import User
from hosteypic_server.users.schemas import SUserRead, SMultiUserRead

router = APIRouter(prefix='/users', tags=['Users'])

current_user = fastapi_users.current_user(active=True)
current_verified_user = fastapi_users.current_user(active=True, verified=True)
current_moderator = RoleManager(is_moderator=True)
current_superuser = fastapi_users.current_user(superuser=True)

@router.get('/')
async def get_users(
        start: int = 0,     #TODO: Control this
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> SMultiUserRead:
    query = alch.select(User).order_by(User.id.asc()).slice(start, end)
    users = (await session.execute(query)).scalars().all()

    return {'count': len(users), 'items': users}

@router.get('/current')
async def get_current_user(user: User = Depends(current_user)) -> SUserRead:
    return user

@router.get('/{id}', responses={404: {"detail": "User not found"}})
async def get_user_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
) -> SUserRead:
    query = alch.select(User).where(User.id == id)
    response = (await session.execute(query)).scalar()
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  detail="User not found"
        )

    return response

@router.delete('/current', status_code=status.HTTP_204_NO_CONTENT)  #TODO: add status_codes
async def delete_current_user(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    await session.delete(user)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_id(
        id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    query = alch.delete(User).where(User.id == id)
    await session.execute(query)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
