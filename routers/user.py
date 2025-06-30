from fastapi import APIRouter, Request, HTTPException, Response
from dto.user_dto import UserCreate
from firebase_admin import auth
from services.user_service import UserSerivice
from decorators.require_user import require_user
import json

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
    
@router.get("/history_list")
@require_user
async def get_user_history(request: Request):
   try:
      user = request.state.user
      res = UserSerivice.get_history(user.get("email"))
      return Response(status_code=201, media_type="application/json", content=json.dumps(res))
   except:
      raise HTTPException(status_code=500, detail="Something went wrong when try to pull history")   
