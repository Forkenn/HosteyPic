from typing import Optional

from fastapi import Depends, Request, status, HTTPException
from fastapi_users import (
    FastAPIUsers, BaseUserManager, IntegerIDMixin, models, schemas
)
from fastapi_users.jwt import generate_jwt
from fastapi_users.db import SQLAlchemyUserDatabase

from hosteypic_server.config import Config
from hosteypic_server.auth.tools import (
    get_user_db, send_email_change_email, send_verify_email, send_reset_password_email
)
from hosteypic_server.auth.config import auth_backend
from hosteypic_server.users.models import User

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = Config.SECRET_TOKEN
    verification_token_secret = Config.SECRET_TOKEN

    async def create(
            self,
            user_create: schemas.UC,
            safe: bool = True,
            request: Optional[Request] = None
    ) -> models.UP:    # Ticket 43
        existing_user = await self.user_db.get_by_username(user_create.username)
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="REGISTER_USERNAME_ALREADY_TAKEN",
            )

        return await super().create(user_create, safe, request)

    async def request_change_email(
            self, user: models.UP, new_email: str, request: Optional[Request] = None
    ):
        token_data = {
            "sub": str(user.id),
            "email": user.email,
            "aud": self.verification_token_audience,
        }

        token = generate_jwt(
            token_data,
            self.verification_token_secret,
            self.verification_token_lifetime_seconds,
        )

        await self.on_after_request_change_email(user, token, new_email, request)

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")
        await send_reset_password_email(token, user.email)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        await send_verify_email(token, user.email)

    async def on_after_request_change_email(
        self, user: User, token: str, new_email, request: Optional[Request] = None    
    ):
        print(f"E-mail change requested for user {user.id}. Verification token: {token}")
        await send_email_change_email(token, user.email, new_email)

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)

class RoleManager:
    def __init__(self, is_moderator: bool = False):
        self.is_moderator: bool = is_moderator

    def __call__(self, user: User = Depends(current_active_user)):
        if not user.is_moderator and self.is_moderator:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted"
            )
        
        return user
