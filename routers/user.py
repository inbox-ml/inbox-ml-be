from fastapi import APIRouter
from dto.user_dto import UserCreate
from services.user_service import UserSerivice

router = APIRouter(prefix="/user")

@router.post("/sign_in")
async def user_signin():
    return

@router.post("/sign_up")
async def user_signup(user: UserCreate):
    print(user)
    res = UserSerivice.create(user)
    print(res)
    return "All good!"