import sqlalchemy as alch

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post

async def get_validate_post(session: AsyncSession, user: User, post_id: int) -> Post:
    query = alch.select(Post).where(Post.id == post_id)
    post: Post = (await session.execute(query)).scalar()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ITEM_NOT_FOUND"
        )
    
    if post.user_id != user.id and not user.is_moderator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="NOT_ALLOWED"
        )
    
    return post
