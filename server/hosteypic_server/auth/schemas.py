import re

from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi_users import schemas

class SUserRead(schemas.BaseUser[int]):
    pass

class SUsername(BaseModel):
    username: str = Field(default=...)

    @field_validator("username")
    @classmethod
    def validate_username(cls, username: str) -> str:
        re_for_usrname: re.Pattern[str] = re.compile(
            r"^(?=(?:.*[A-Za-z]){1,})[A-Za-z\d]{5,30}$"
        )
        if not re_for_usrname.match(username):
            raise ValueError("Username does not meet the requirements")
        return username

class SUserCreate(SUsername, schemas.CreateUpdateDictModel):
    email: EmailStr
    password: str = Field(default=...)

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        re_for_pw: re.Pattern[str] = re.compile(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*#?&]{6,}$"
        )
        if not re_for_pw.match(password):
            raise ValueError("Password does not meet the requirements")
        return password

class SUserUpdate(schemas.BaseUserUpdate):
    pass

class SUserRequestChangeEmail(BaseModel):
    new_email: EmailStr

class SUserChangeEmail(SUserRequestChangeEmail):
    token: str


class SUserChangePassword(BaseModel):
    old: str
    new: str