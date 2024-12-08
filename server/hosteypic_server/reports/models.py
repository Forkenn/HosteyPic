from datetime import datetime, timezone

import sqlalchemy as alch
import sqlalchemy.orm as orm

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.sql import func

from hosteypic_server.database import Base
from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post

class Report(Base):
    __tablename__ = 'reports'
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    body: orm.Mapped[str] = orm.mapped_column(String(300))
    timestamp: orm.Mapped[datetime] = orm.mapped_column(
        DateTime(timezone=True), default=func.now()
    )

    user_id: orm.Mapped[int] = orm.mapped_column(
        ForeignKey(User.id, ondelete='CASCADE'), nullable=True
    )
    post_id: orm.Mapped[int] = orm.mapped_column(
        ForeignKey(Post.id, ondelete='CASCADE'),
    )

    report_author = orm.relationship("User", viewonly=True)
