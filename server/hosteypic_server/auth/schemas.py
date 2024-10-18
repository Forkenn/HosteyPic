from pydantic import BaseModel, Field, EmailStr
from fastapi_users import schemas

class SUserRead(schemas.BaseUser[int]):
    pass

class SUserCreate(schemas.CreateUpdateDictModel):
    username: str = Field(
        default=...,
        min_length=5,
        max_length=10,
        description="Username from 5 to 10 symbols"
    )
    email: EmailStr
    password: str

class SUserUpdate(schemas.BaseUserUpdate):
    pass

class SUserRequestChangeEmail(BaseModel):
    new_email: EmailStr

class SUserChangeEmail(SUserRequestChangeEmail):
    token: str
