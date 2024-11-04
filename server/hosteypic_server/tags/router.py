import sqlalchemy as alch

from typing import List

from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.database import get_async_session
from hosteypic_server.exceptions import (
    MaxObjectsException, AlreadyExistException, NotFoundException
)

from hosteypic_server.config import Config
from hosteypic_server.users.models import User
from hosteypic_server.tags.models import Tag
from hosteypic_server.tags.schemas import STagCreate

router = APIRouter(prefix='/tags', tags=['Tags'])

current_optional_user = fastapi_users.current_user(optional=True, active=True)
current_superuser = fastapi_users.current_user(superuser=True)

@router.get('')
async def get_tags(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
):
    query = alch.select(Tag)

    tags = (await session.execute(query)).scalars().all()
    return {"count": len(tags), "items": tags}

@router.post('')
async def upload_new_tag(
        data: STagCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    if (await Tag.tags_count()) >= Config.MAX_TAGS_COUNT:
        raise MaxObjectsException()
    
    query = alch.select(Tag).where(Tag.name == data.name)
    tag_resp = (await session.execute(query)).scalar()
    if tag_resp:
        raise AlreadyExistException()

    tag = Tag(name=data.name)
    session.add(tag)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/{tag_id}')
async def delete_tag_by_id(
        tag_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    tag = await session.get(Tag, tag_id)
    if not tag:
        raise NotFoundException()
    
    await session.delete(tag)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
