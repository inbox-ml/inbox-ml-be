from typing import Optional
from pydantic import BaseModel, PositiveInt

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    age: PositiveInt | None

class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[PositiveInt] = None

class User(UserCreate):
    pass    