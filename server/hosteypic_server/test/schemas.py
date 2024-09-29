import re
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional

class STest(BaseModel):
    id: int
    username: str = Field(default=..., min_length=1, max_length=10, description="Никнейм от 1 до 10 символов")
    phone_number: str = Field(default=..., description="Номер телефона в международном формате с '+'")
    email: EmailStr = Field(default=..., description="Электронная почта")
    year: int = Field(default=..., ge=2020, description="Год не меньше 2020")
    random_num: int = Field(default=..., ge=1, le=55, description="Случайное число в диапазоне от 1 до 5")
    optional_field: Optional[str] = Field(
        default=None, max_length=500, description="Опциональное поле до 500 символов"
    )

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values
