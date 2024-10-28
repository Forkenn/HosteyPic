import sqlalchemy as alch

from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.posts.models import Post
from hosteypic_server.exceptions import NotFoundException

async def get_object_by_id(post_id: int, session: AsyncSession) -> Post:
    query = alch.select(Post).where(Post.id == post_id)
    post = (await session.execute(query)).scalar()
    if not post:
        raise NotFoundException()
    
    return post
