from typing import Optional

from fastapi import Depends, Request, status, HTTPException
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from hosteypic_server.config import Config
from hosteypic_server.auth.tools import get_user_db
# from hosteypic_server.auth.config import fastapi_users
from hosteypic_server.users.models import User

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = Config.SECRET_TOKEN
    verification_token_secret = Config.SECRET_TOKEN

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        # TODO: E-mail send!
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        # TODO: E-mail send!
        print(f"Verification requested for user {user.id}. Verification token: {token}")

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
