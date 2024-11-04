from datetime import datetime, timezone

import sqlalchemy as alch
import sqlalchemy.orm as orm

from typing import List

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.sql import func

from hosteypic_server.database import Base, async_session_maker
from hosteypic_server.mixins import ModelMixin
from hosteypic_server.users.models import User
from hosteypic_server.tags.models import Tag, tags_posts

class Post(Base, ModelMixin):
    __tablename__ = 'posts'
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(String(100))
    body: orm.Mapped[str] = orm.mapped_column(String(500))
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    attachment: orm.Mapped[str] = orm.mapped_column(String(256))
    user_id: orm.Mapped[int] = orm.mapped_column(
        ForeignKey(User.id, ondelete='CASCADE'), index=True
    )

    author: orm.Mapped['User'] = orm.relationship(back_populates='posts')

    # many-to-many relationship to User, bypassing the Like class
    liked_by: orm.Mapped[List["User"]] = orm.relationship(
        secondary="likes", back_populates="liked", viewonly=True
    )

    # association between Post -> Like -> User
    user_associations: orm.Mapped[List["Like"]] = orm.relationship(
        back_populates="post"
    )

    tags: orm.Mapped[List["Tag"]] = orm.relationship(secondary=tags_posts)

    async def liked_flag(self, user: User) -> bool:
        query = alch.select(Like).where(
            alch.and_(Like.post_id == self.id, Like.user_id == user.id)
        )

        async with async_session_maker() as session:
            is_liked = (await session.execute(query)).scalar() is not None

        return is_liked

    async def deletable_flag(self, user: User) -> bool:
        if self.user_id != user.id and not user.is_moderator:
            return False
        
        return True
        
    async def editable_flag(self, user: User) -> bool:
        if not (await self.deletable_flag(user)):
            return False

        delta = datetime.now(timezone.utc) - self.timestamp
        return not delta.days

    def __repr__(self):
        return f"Post with id:{self.id}"
    
from hosteypic_server.likes.models import Like

Post.likes_count = orm.column_property(
    alch.select(func.count(Like.post_id))
    .where(Post.id == Like.post_id)
    .scalar_subquery()
)
