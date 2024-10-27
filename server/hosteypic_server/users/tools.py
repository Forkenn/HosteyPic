import sqlalchemy as alch

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.users.models import User
from hosteypic_server.exceptions import NotFoundException

async def get_object_by_id(user_id: int, session: AsyncSession) -> User:
    query = alch.select(User).where(User.id == user_id)
    user = (await session.execute(query)).scalar()
    if not user:
        raise NotFoundException()
    
    return user
