import re

from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr, field_validator

from hosteypic_server.auth.schemas import SUsername

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
    about_me: Optional[str] = Field(default=None, max_length=140)
    vk_link: Optional[str] = Field(default=None, max_length=140)
    ok_link: Optional[str] = Field(default=None, max_length=140)
    github_link: Optional[str] = Field(default=None, max_length=140)
    gitlab_link: Optional[str] = Field(default=None, max_length=140)

    @classmethod
    def link_validator(cls, link: str | None, regex: str) -> str | None:
        if not link:
            return link
        
        pattern: re.Pattern[str] = re.compile(regex)
        if not pattern.match(link):
            raise ValueError("Link does not meet the requirements")
        
        return link

    @field_validator("vk_link")
    @classmethod
    def validate_vk_link(cls, vk_link: str) -> str | None:
        regex = r"^$|^(https?://vk\.com/)([a-zA-Z0-9._]{4,30}|id\d{1,28})$"
        return cls.link_validator(vk_link, regex)
    
    @field_validator("ok_link")
    @classmethod
    def validate_ok_link(cls, ok_link: str) -> str | None:
        regex = r"^$|^(https?://ok\.ru/profile/)(\d{1,30})$"
        return cls.link_validator(ok_link, regex)
    
    @field_validator("github_link")
    @classmethod
    def validate_github_link(cls, github_link: str) -> str | None:
        regex = r"^$|^(https?://github\.com/)([a-zA-Z0-9](?:-?[a-zA-Z0-9]){0,38})$"
        return cls.link_validator(github_link, regex)
    
    @field_validator("gitlab_link")
    @classmethod
    def validate_gitlab_link(cls, gitlab_link: str) -> str | None:
        regex = r"^$|^(https?://gitlab\.com/)([a-zA-Z0-9](?:[._-]?[a-zA-Z0-9]){0,29})$"
        return cls.link_validator(gitlab_link, regex)

class SUserUsernameEdit(SUsername):
    pass

class SUserEmailEdit(BaseModel):
    email: EmailStr
