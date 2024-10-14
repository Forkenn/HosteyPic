import sqlalchemy.orm as orm
from sqlalchemy import String, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable

from hosteypic_server.database import Base

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'users'
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(String(15), index=True, unique=True)
    email: orm.Mapped[str] = orm.mapped_column(String(120), index=True, unique=True)
    about_me: orm.Mapped[str] = orm.mapped_column(String(140), nullable=True)
    avatar_link: orm.Mapped[str] = orm.mapped_column(String(256), nullable=True)
    vk_link: orm.Mapped[str] = orm.mapped_column(String(128), nullable=True)
    ok_link: orm.Mapped[str] = orm.mapped_column(String(128), nullable=True)
    github_link: orm.Mapped[str] = orm.mapped_column(String(128), nullable=True)
    gitlab_link: orm.Mapped[str] = orm.mapped_column(String(128), nullable=True)
    is_moderator: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)

    # fastapi-users fields by default:
    # hashed_password: orm.Mapped[str] = orm.mapped_column(String(256))
    # is_verified: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)
    # is_active: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)
    # is_superuser: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"User with id:{self.id}"
