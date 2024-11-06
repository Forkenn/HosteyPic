from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr

class SUserRead(BaseModel):
    id: int
    username: str
    about_me: str | None
    avatar: str | None
    vk_link: str | None
    ok_link: str | None
    github_link: str | None
    gitlab_link: str | None
    is_active: bool
    is_verified: bool
    is_moderator: bool

class SUserReadSingle(SUserRead):
    is_following: Optional[bool] = False
    followers_count: Optional[int] = 0

class SUserReadFull(SUserRead):
    is_superuser: bool
    email: str

class SMultiUserRead(BaseModel):
    count: int
    items: List[SUserRead]

class SUserEdit(BaseModel):
    about_me: str | None
    vk_link: str | None
    ok_link: str | None
    github_link: str | None
    gitlab_link: str | None

class SUserUsernameEdit(BaseModel):
    username: str = Field(
        default=...,
        min_length=5,
        max_length=30,
        description="Username from 5 to 30 symbols"
    )

class SUserEmailEdit(BaseModel):
    email: EmailStr
