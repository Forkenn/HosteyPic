from typing import List

from pydantic import BaseModel

class SUserRead(BaseModel):
    id: int
    username: str
    email: str
    about_me: str | None
    avatar_link: str | None
    vk_link: str | None
    ok_link: str | None
    github_link: str | None
    gitlab_link: str | None
    is_active: bool
    is_verified: bool
    is_moderator: bool
    is_superuser: bool

class SMultiUserRead(BaseModel):
    count: int
    items: List[SUserRead]
