import sqlalchemy as alch

from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.exceptions import NotFoundException

async def get_object_by_id(id: int, table: Callable, session: AsyncSession) -> Callable:
    query = alch.select(table).where(table.id == id)
    db_object = (await session.execute(query)).scalar()
    if not db_object:
        raise NotFoundException()
    
    return db_object
