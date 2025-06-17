from pydantic import BaseModel, PositiveInt

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    age: PositiveInt | None


