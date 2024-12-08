import sqlalchemy as alch

from fastapi import APIRouter, status, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from hosteypic_server.exceptions import NotFoundException
from hosteypic_server.database import get_async_session
from hosteypic_server.auth.manager import fastapi_users, RoleManager
from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post
from hosteypic_server.reports.models import Report
from hosteypic_server.reports.schemas import SReports

router = APIRouter(prefix='/reports', tags=['Reports'])

current_optional_user = fastapi_users.current_user(optional=True, active=True)
current_moderator = RoleManager(is_moderator=True)

@router.get('')
async def get_reports(
        start: int = 0,
        end: int = 5,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
) -> SReports:
    query = (
        alch.select(Report)
        .order_by(Report.timestamp.desc())
        .options(
            joinedload(Report.report_author)
        )
        .slice(start, end)
    )
    reports = (await session.execute(query)).scalars().all()

    return {'count': len(reports), 'items': reports}

@router.post('')
async def create_report(
        post_id: int,
        text_body: str,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_optional_user)
):
    query = alch.select(Post.id).where(Post.id == post_id)
    post = (await session.execute(query)).first()

    if not post:
        raise NotFoundException()
    
    report = Report(
        body=text_body,
        post_id=post_id,
        user_id=(user.id if user else None)
    )

    session.add(report)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.delete('')
async def delete_report_by_id(
        report_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_moderator)
):
    query = alch.select(Report).where(Report.id == report_id)
    report = (await session.execute(query)).scalar()

    if not report:
        raise NotFoundException()
    
    await session.delete(report)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
