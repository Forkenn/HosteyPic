from typing import List, Optional
from datetime import datetime

from fastapi import Query
from pydantic import BaseModel, Field

class STagRead(BaseModel):
    id: int
    name: str

class SPostPreview(BaseModel):
    id: int
    user_id: int
    attachment: str
    is_deletable: bool = False
    is_editable: bool = False

class SPostRead(SPostPreview):
    is_liked: bool = False
    likes_count: int
    title: str
    body: str
    timestamp: datetime
    tags_list: List[STagRead] = None

class SPostsPreviews(BaseModel):
    count: int
    items: List[SPostPreview]

class SPostCreate(BaseModel):
    title: str = Field(
        default=...,
        min_length=4,
        max_length=100,
        description="Title from 4 to 100 symbols"
    )
    body: str = Field(
        default=...,
        min_length=0,
        max_length=500,
        description="Body from 0 to 500 symbols"
    )
    tags_list: Optional[List[int]] = Field(
        Query(
            default_factory=list,
            min_items=0,
            max_items=10,
            alias='tags',
            description="Tags ids. Max 10 elements"
        )
    )
