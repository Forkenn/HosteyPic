from pydantic import BaseModel, Field

class STagCreate(BaseModel):
    name: str = Field(
        default=...,
        min_length=3,
        max_length=50,
        description="Tag name from 3 to 50 symbols"
    )
