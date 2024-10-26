from typing import List
from datetime import datetime

from pydantic import BaseModel

class SPostRead(BaseModel):
    id: int
    user_id: int
    title: str
    body: str
    attachment: str
    timestamp: datetime

class SPostsRead(BaseModel):
    count: int
    items: List[SPostRead]

class SPostCreate(BaseModel):
    title: str
    body: str
