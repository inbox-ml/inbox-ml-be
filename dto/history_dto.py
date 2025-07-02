from typing import Optional
from pydantic import BaseModel

class HistoryCreate(BaseModel):
    category: str
    is_scam: bool
    summary: str
    summary_title: str

class History(HistoryCreate):
    pass    