from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, UploadFile, Depends, Response, status
from hosteypic_server.database import get_async_session
from hosteypic_server.auth.manager import fastapi_users
from hosteypic_server.users.models import User
from hosteypic_server.dataset.tools import DatasetManager

router = APIRouter(prefix='/dataset', tags=['Dataset'])

current_superuser = fastapi_users.current_user(superuser=True)

@router.post('')
async def fill_dataset(
        data: UploadFile,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser)
):
    return await DatasetManager.load_csv(data, session=session)

@router.post('/likes')
async def fill_likes(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser) 
):
    await DatasetManager.add_likes(session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/followers')
async def fill_followers(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_superuser) 
):
    await DatasetManager.add_followers(session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
