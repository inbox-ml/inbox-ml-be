from fastapi import APIRouter

router = APIRouter(prefix="/user")

@router.post("/sign_in")
async def user_signin():
    return

@router.post("/sign_up")
async def user_signup():
    return