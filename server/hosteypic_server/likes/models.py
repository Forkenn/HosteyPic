import sqlalchemy as alch
import sqlalchemy.orm as orm

from hosteypic_server.database import Base
from hosteypic_server.mixins import ModelMixin


#likes = alch.Table(
#    'likes', Base.metadata,
#    alch.Column('post_id', alch.Integer, alch.ForeignKey('posts.id', ondelete='CASCADE'),
#        primary_key=True),
#    alch.Column('user_id', alch.Integer, alch.ForeignKey('users.id', ondelete='CASCADE'),
#        primary_key=True)
#)
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#combining-association-object-with-many-to-many-access-patterns

class Like(Base, ModelMixin):
    __tablename__ = "likes"

    post_id: orm.Mapped[int] = orm.mapped_column(
        alch.ForeignKey("posts.id", ondelete='CASCADE'), primary_key=True
    )
    user_id: orm.Mapped[int] = orm.mapped_column(
        alch.ForeignKey("users.id", ondelete='CASCADE'), primary_key=True
    )

    # association between Like -> User
    user: orm.Mapped["User"] = orm.relationship(back_populates="post_associations")

    # association between Like -> Post
    post: orm.Mapped["Post"] = orm.relationship(back_populates="user_associations")

from hosteypic_server.posts.models import Post
from hosteypic_server.users.models import User
