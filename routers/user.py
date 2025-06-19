from fastapi import APIRouter
from dto.user_dto import UserCreate
from services.user_service import UserSerivice

router = APIRouter(prefix="/user")

@router.post("/sign_in")
async def user_signin():
    return

@router.post("/sign_up")
def user_signup(user: UserCreate):
    res = UserSerivice.create(user)
    return "All good!"


@router.get("/{id}")
def get_user(id: str):
    res = UserSerivice.get(id)
    return res