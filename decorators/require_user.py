from functools import wraps
from fastapi import HTTPException, Request
from firebase_admin import auth
from services.user_service import UserSerivice
from typing import Optional

def require_user(func):
    print("Before calling the function.")
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Optional[Request] = kwargs.get("request")

        if not request:
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
        
        if not isinstance(request, Request):
            raise HTTPException(status_code=400, detail="Request object is required")
        
        decoded_token = auth.verify_id_token(request.state.token)
        user = await UserSerivice.get(decoded_token.get("email"))

        if not user:
            raise HTTPException(status_code=500, detail="Could not get user data")
        
        request.state.user = user

        res = await func(*args, **kwargs)
        print("After calling the function.")
        return res

    return wrapper