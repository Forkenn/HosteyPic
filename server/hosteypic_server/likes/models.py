import sqlalchemy as alch
import sqlalchemy.orm as orm
from fastapi_users.db import SQLAlchemyBaseUserTable

from hosteypic_server.database import Base, async_session_maker
from hosteypic_server.mixins import ModelMixin

likes = alch.Table(
    'likes', Base.metadata,
    alch.Column('post_id', alch.Integer, alch.ForeignKey('posts.id', ondelete='CASCADE'),
        primary_key=True),
    alch.Column('user_id', alch.Integer, alch.ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True)
)
