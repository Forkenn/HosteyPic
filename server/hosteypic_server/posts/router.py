from fastapi import APIRouter, UploadFile, HTTPException, status, Depends, Response

import sqlalchemy as alch
import sqlalchemy.orm as orm
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.database import get_async_session
from hosteypic_server.auth.manager import fastapi_users
from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post
from hosteypic_server.posts.schemas import SPostRead, SPostsRead, SPostCreate
from hosteypic_server.posts.tools import get_validate_post

router = APIRouter(prefix='/posts', tags=['Posts'])

current_user = fastapi_users.current_user(active=True, verified=True)

@router.get('/')
async def get_last_posts(
        start: int,
        end: int,
        session: AsyncSession = Depends(get_async_session)
) -> SPostsRead:
    query = alch.select(Post).order_by(Post.timestamp.asc()).slice(start, end)
    posts = (await session.execute(query)).scalars().all()

    return {'count': len(posts), 'items': posts}

@router.get('/followed')
async def get_followed_posts(
        start: int,
        end: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> SPostsRead:
    Author = orm.aliased(User)
    Follower = orm.aliased(User)

    query = alch.select(Post).join(Post.author.of_type(Author)).join(
        Author.followers.of_type(Follower), isouter=True
    ).where(alch.or_(
        Follower.id == user.id, Author.id == user.id
    )).group_by(Post).order_by(Post.timestamp.desc()).slice(start, end)

    posts = (await session.execute(query)).scalars().all()

    return {'count': len(posts), 'items': posts}

@router.get('/{post_id}')
async def get_post_by_id(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> SPostRead:
    query = alch.select(Post).where(Post.id == post_id)

    return (await session.execute(query)).scalar()

@router.post('/')
async def create_post(
        attachment: UploadFile,
        post_data: SPostCreate = Depends(),
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    if attachment.content_type not in ('image/jpeg', 'image/png'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="INVALID_FILE_TYPE"
        )
    
    post_dict = post_data.model_dump()
    post_dict.update({'user_id': user.id, 'attachment': 'test.jpg'})

    new_post = Post(**post_dict)
    session.add(new_post)
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{post_id}')
async def edit_post_by_id(
        post_id: int,
        post_data: SPostCreate = Depends(),
        attachment: UploadFile = None,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    if attachment and attachment.content_type not in ('image/jpeg', 'image/png'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="INVALID_FILE_TYPE"
        )
    
    # attachment upload|delete
    post: Post = await get_validate_post(session, user, post_id)
    await post.update(**post_data.model_dump())
    await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/{post_id}')
async def delete_post_by_id(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    post: Post = await get_validate_post(session, user, post_id)
    await session.delete(post)
    await session.commit()                                  # flush didn't work

    return Response(status_code=status.HTTP_204_NO_CONTENT)
