import sqlalchemy as alch
import sqlalchemy.orm as orm

from typing import List

from fastapi_users.db import SQLAlchemyBaseUserTable

from hosteypic_server.database import Base, async_session_maker
from hosteypic_server.mixins import ModelMixin

followers = alch.Table(
    'followers', Base.metadata,
    alch.Column('follower_id', alch.Integer, alch.ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True),
    alch.Column('followed_id', alch.Integer, alch.ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True)
)

email_allowlist = alch.Table(
    'email_allowlist', Base.metadata,
    alch.Column('id', alch.Integer, primary_key=True),
    alch.Column('email', alch.String(120), index=True, unique=True)
)

class User(SQLAlchemyBaseUserTable[int], ModelMixin, Base):
    __tablename__ = 'users'
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(alch.String(31), index=True, unique=True)
    email: orm.Mapped[str] = orm.mapped_column(alch.String(120), index=True, unique=True)
    about_me: orm.Mapped[str] = orm.mapped_column(alch.String(140), nullable=True)
    avatar: orm.Mapped[str] = orm.mapped_column(
        alch.String(256), nullable=True, server_default=alch.text("'default.jpg'")
    )
    vk_link: orm.Mapped[str] = orm.mapped_column(alch.String(128), nullable=True)
    ok_link: orm.Mapped[str] = orm.mapped_column(alch.String(128), nullable=True)
    github_link: orm.Mapped[str] = orm.mapped_column(alch.String(128), nullable=True)
    gitlab_link: orm.Mapped[str] = orm.mapped_column(alch.String(128), nullable=True)
    is_moderator: orm.Mapped[bool] = orm.mapped_column(alch.Boolean(), default=False)

    posts: orm.WriteOnlyMapped['Post'] = orm.relationship(back_populates='author')

    # many-to-many relationship to Post, bypassing the Like class
    liked: orm.Mapped[List["Post"]] = orm.relationship(
        secondary="likes", back_populates="liked_by", viewonly=True
    )

    # association between User -> Like -> Post
    post_associations: orm.Mapped[List["Like"]] = orm.relationship(
        back_populates="user"
    )

    following: orm.WriteOnlyMapped['User'] = orm.relationship(
        secondary=followers, primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        back_populates='followers'
    )
    followers: orm.WriteOnlyMapped['User'] = orm.relationship(
        secondary=followers, primaryjoin=(followers.c.followed_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        back_populates='following'
    )

    # fastapi-users fields by default:
    # hashed_password: orm.Mapped[str] = orm.mapped_column(String(256))
    # is_verified: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)
    # is_active: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)
    # is_superuser: orm.Mapped[bool] = orm.mapped_column(Boolean(), default=False)

    async def is_following(self, user) -> bool:
        query = self.following.select().where(User.id == user.id)
        async with async_session_maker() as session:
            flag: bool = await session.scalar(query) is not None

        return flag

    async def follow(self, user) -> None:
        if not await self.is_following(user):
            self.following.add(user)

    async def unfollow(self, user) -> None:
        if await self.is_following(user):
            self.following.remove(user)

    async def followers_count(self) -> int:
        query = alch.select(alch.func.count()).select_from(
            self.followers.select().subquery()
        )
        async with async_session_maker() as session:
            count: int = await session.scalar(query)
        
        return count

    async def following_count(self) -> int:
        query = alch.select(alch.func.count()).select_from(
            self.following.select().subquery()
        )
        async with async_session_maker() as session:
            count: int = await session.scalar(query)

        return count

    def __repr__(self):
        return f"User with id: {self.id}"

from hosteypic_server.posts.models import Post
from hosteypic_server.likes.models import Like
