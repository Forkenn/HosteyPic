from datetime import datetime

from pydantic import BaseModel

class SReportAuthor(BaseModel):
    username: str

class SReport(BaseModel):
    id: int
    user_id: int | None = None
    post_id: int
    report_author: SReportAuthor | None = None
    body: str
    timestamp: datetime

class SReports(BaseModel):
    count: int
    items: list[SReport]
