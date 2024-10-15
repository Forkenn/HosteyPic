import sqlalchemy as alch

from pydantic import BaseModel

from hosteypic_server.database import async_session_maker
from hosteypic_server.users.models import User

async def change_user(user_id: int, data: BaseModel):
    async with async_session_maker() as session:
        query = alch.update(User).where(User.id == user_id).values(**data.model_dump())
        await session.execute(query)
        await session.commit()
