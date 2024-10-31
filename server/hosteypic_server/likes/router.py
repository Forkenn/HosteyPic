import sqlalchemy as alch
import sqlalchemy.orm as orm

from fastapi import APIRouter, status, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.database import get_async_session
from hosteypic_server.exceptions import AlreadyExistException, NotFoundException
from hosteypic_server.auth.manager import fastapi_users
from hosteypic_server.users.models import User
from hosteypic_server.likes.models import Like

router = APIRouter(prefix='/likes', tags=['Likes'])

current_user = fastapi_users.current_user(active=True, verified=True)
@router.post('/posts/{post_id}')
async def set_like_by_id(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = alch.select(Like).where(Like.post_id == post_id)
    like_resp = (await session.execute(query)).scalar()

    if like_resp:
        raise AlreadyExistException()

    like = Like(**{'post_id': post_id, 'user_id': user.id})
    session.add(like)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/posts/{post_id}')
async def delete_like_by_id(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = alch.select(Like).where(Like.post_id == post_id)
    like_resp = (await session.execute(query)).scalar()

    if not like_resp:
        raise NotFoundException()

    await session.delete(like_resp)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
