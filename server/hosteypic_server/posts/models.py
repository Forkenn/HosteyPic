from datetime import datetime, timezone

import sqlalchemy as alch
import sqlalchemy.orm as orm
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.sql import func

from hosteypic_server.database import Base
from hosteypic_server.mixins import ModelMixin
from hosteypic_server.users.models import User

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

    # tags: orm.WriteOnlyMapped[Tag] = orm.relationship(back_populates='post')

    async def __repr__(self):
        return f"Post with id:{self.id}"
