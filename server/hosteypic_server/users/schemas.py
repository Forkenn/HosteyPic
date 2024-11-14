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

    @field_validator("vk_link")
    @classmethod
    def validate_vk_link(cls, vk_link: str) -> str:
        re_for_usrname: re.Pattern[str] = re.compile(
            r"^(https?://vk\.com/)([a-zA-Z0-9._]{4,30}|id\d{1,28})$"
        )
        if not re_for_usrname.match(vk_link):
            raise ValueError("VK link does not meet the requirements")
        return vk_link
    
    @field_validator("ok_link")
    @classmethod
    def validate_ok_link(cls, ok_link: str) -> str:
        re_for_usrname: re.Pattern[str] = re.compile(
            r"^(https?://ok\.ru/profile/)(\d{1,30})$"
        )
        if not re_for_usrname.match(ok_link):
            raise ValueError("OK link does not meet the requirements")
        return ok_link
    
    @field_validator("github_link")
    @classmethod
    def validate_github_link(cls, github_link: str) -> str:
        re_for_usrname: re.Pattern[str] = re.compile(
            r"^(https?://github\.com/)([a-zA-Z0-9](?:-?[a-zA-Z0-9]){0,38})$"
        )
        if not re_for_usrname.match(github_link):
            raise ValueError("GitHub link does not meet the requirements")
        return github_link
    
    @field_validator("gitlab_link")
    @classmethod
    def validate_gitlab_link(cls, ok_link: str) -> str:
        re_for_usrname: re.Pattern[str] = re.compile(
            r"^(https?://gitlab\.com/)([a-zA-Z0-9](?:[._-]?[a-zA-Z0-9]){0,29})$"
        )
        if not re_for_usrname.match(ok_link):
            raise ValueError("GitLab link does not meet the requirements")
        return ok_link

class SUserUsernameEdit(SUsername):
    pass

class SUserEmailEdit(BaseModel):
    email: EmailStr
