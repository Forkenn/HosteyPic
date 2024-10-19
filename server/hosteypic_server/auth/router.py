from fastapi import APIRouter, HTTPException, status, Response, Depends

from fastapi_users import exceptions
from fastapi_users.password import PasswordHelper

import sqlalchemy as alch
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.database import get_async_session
from hosteypic_server.auth.manager import fastapi_users, UserManager
from hosteypic_server.auth.schemas import (
    SUserRequestChangeEmail, SUserChangeEmail, SUserRead, SUserChangePassword
)
from hosteypic_server.users.models import User

router = APIRouter(prefix='/auth', tags=['Auth'])

current_user = fastapi_users.current_user(active=True)
current_user_verified = fastapi_users.current_user(active=True, verified=True)

responses ={
    404: {"description": "Item not found"},
    401: {"description": "Missing token or inactive/unverified user."},
    400: {"description": "Bad Request"},
    204: {"description": "Successful Response"},
    202: {"description": "Successful Response"}
}

@router.post('/change-password', responses=responses)
async def change_password(
        data: SUserChangePassword,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    password_helper = PasswordHelper()

    if not password_helper.verify_and_update(data.old, user.hashed_password)[0]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="LOGIN_BAD_CREDENTIALS"
        )
    
    query = alch.update(User).values(
        hashed_password=password_helper.hash(data.new)
    ).where(User.id == user.id)

    await session.execute(query)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/request-change-email', responses=responses)
async def request_change_email(
        data: SUserRequestChangeEmail,
        session: AsyncSession = Depends(get_async_session),
        user_manager: UserManager = Depends(fastapi_users.get_user_manager),
        user: User = Depends(current_user_verified)
):
    query = alch.select(User).where(User.email == data.new_email)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EMAIL_ALREADY_TAKEN"
        )

    await user_manager.request_change_email(user, data.new_email)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/change-email', responses=responses)
async def change_email(
        data: SUserChangeEmail,
        session: AsyncSession = Depends(get_async_session),
        user_manager: UserManager = Depends(fastapi_users.get_user_manager),
        user: User = Depends(current_user_verified)
) -> SUserRead:
    try:
        await user_manager.verify(data.token)

    except exceptions.UserAlreadyVerified:
        pass

    except exceptions.InvalidVerifyToken:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="VERIFY_USER_BAD_TOKEN"
        )
    
    query = alch.select(User).where(User.email == data.new_email)
    user_check = (await session.execute(query)).scalar()

    if user_check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EMAIL_ALREADY_TAKEN"
        )
    
    query = alch.update(User).where(User.id == user.id).values(
        email=data.new_email
    )

    await session.execute(query)
    await session.commit()

    query = alch.select(User).where(User.id == user.id)
    return (await session.execute(query)).scalar()
