import sqlalchemy as alch

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.users.models import User

async def get_object_by_id(user_id: int, session: AsyncSession) -> User:
    query = alch.select(User).where(User.id == user_id)
    user = (await session.execute(query)).scalar()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  detail="ITEM_NOT_FOUND"
        )
    
    return user
