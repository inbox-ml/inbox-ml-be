from typing import Optional
from pydantic import BaseModel

class HistoryCreate(BaseModel):
    category: str
    is_scam: bool
    summary: str
    summary_title: str

class History(HistoryCreate):
    created_at: str
    updated_at: str
    status: str


class ArchiveHistory(BaseModel):
    item_id: str