from typing import Optional

from fastapi import Depends
from fastapi_users import models
from fastapi_users.db import SQLAlchemyUserDatabase

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.config import Config
from hosteypic_server.database import get_async_session
from hosteypic_server.email import send_email
from hosteypic_server.users.models import User

class HosteypicUserDatabase(SQLAlchemyUserDatabase):    # Ticket 43
    async def get_by_username(self, username: str) -> Optional[models.UP]:
        statement = select(self.user_table).where(
            func.lower(self.user_table.username) == func.lower(username)
        )
        return await self._get_user(statement)

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield HosteypicUserDatabase(session, User)

async def send_email_change_email(token: str, email: str, new_email: str):
    change_link = Config.CHANGE_EMAIL_URL.format(token=token, new_email=new_email)
    subject = "Запрос на смену E-mail"
    sender = "admin@hosteypic.ru"
    await send_email(
        subject=subject,
        sender=sender,
        recipients=[new_email],
        text_body=f'Перейдите по ссылке, чтобы подтвердить смену E-mail: {change_link}',
        html_body=''
    )

    await send_email(
        subject=subject,
        sender=sender,
        recipients=[email],
        text_body=(
            f'Был осуществлен запрос на смену E-mail на {new_email}.\n'
            'Если Вы не отправляли запрос, свяжитесь с тех. поддержкой.'
        ),
        html_body=''
    )

async def send_verify_email(token: str, email: str):
    verify_link = Config.VERIFY_URL.format(token=token)
    await send_email(
        subject="Подтверждение E-mail",
        sender="admin@hosteypic.ru",
        recipients=[email],
        text_body=f'Перейдите по ссылке, чтобы подтвердить E-mail: {verify_link}',
        html_body=''
    )

async def send_reset_password_email(token: str, email: str):
    reset_link = Config.RESET_URL.format(token=token)
    await send_email(
        subject="Сброс пароля HosteyPic",
        sender="admin@hosteypic.ru",
        recipients=[email],
        text_body=(
            f'Перейдите по ссылке, чтобы сбросить пароль: {reset_link}\n'
            'Если Вы не отправляли запрос, игнорируйте данное письмо.'
        ),
        html_body=''
    )
