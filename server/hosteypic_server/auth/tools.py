from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.config import Config
from hosteypic_server.database import get_async_session
from hosteypic_server.email import send_email
from hosteypic_server.users.models import User

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def send_email_change_email(token: str, email: str, new_email: str):
    change_link = Config.RESET_EMAIL_PATH.format(token=token, new_email=new_email)
    await send_email(
        subject="Запрос на смену E-mail",
        sender="admin@hosteypic.ru",
        recipients=[email],
        text_body=f'Перейдите по ссылке, чтобы подтвердить смену E-mail: {change_link}',
        html_body=''
    )

async def send_verify_email(token: str, email: str):
    verify_link = Config.VERIFY_PATH.format(token=token)
    await send_email(
        subject="Подтверждение E-mail",
        sender="admin@hosteypic.ru",
        recipients=[email],
        text_body=f'Перейдите по ссылке, чтобы подтвердить E-mail: {verify_link}',
        html_body=''
    )
