from fastapi import APIRouter, Request, HTTPException
from dto.user_dto import UserCreate
from firebase_admin import auth
from services.user_service import UserSerivice

router = APIRouter(prefix="/user")

@router.post("/sign_in")
async def user_signin():
    return

@router.post("/sign_up")
def user_signup(user: UserCreate):
    res = UserSerivice.create(user)
    return "All good!"


@router.get("/")
async def get_user(request: Request):
    token = request.state.token

    try:
     decoded_token = auth.verify_id_token(token)
     res = UserSerivice.get(decoded_token.get("email"))
     if not res:
        raise HTTPException(status_code=500, detail="Could not get user data")
     return res

    except:
        raise HTTPException(status_code=401, detail="Invalid token")