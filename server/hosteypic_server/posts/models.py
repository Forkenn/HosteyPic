import sqlalchemy.orm as orm
from sqlalchemy import ForeignKey

from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String

from hosteypic_server.database import Base
from hosteypic_server.users.models import User

class Post(Base):
    __tablename__ = 'posts'
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(String(100))
    body: orm.Mapped[str] = orm.mapped_column(String(500))
    timestamp: orm.Mapped[Optional[datetime]] = orm.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    attachment: orm.Mapped[str] = orm.mapped_column(String(256))
    user_id: orm.Mapped[int] = orm.mapped_column(
        ForeignKey(User.id, ondelete='CASCADE'), index=True
    )

    author: orm.Mapped['User'] = orm.relationship(back_populates='posts')

    # tags: orm.WriteOnlyMapped[Tag] = orm.relationship(back_populates='post')

    def __repr__(self):
        return f"Post with id:{self.id}"
