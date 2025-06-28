from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthTokenMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        token = request.headers.get("Authorization")
        if token is None or not token.startswith("Bearer"):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

        request.state.token = token.split(" ")[1]
        response = await call_next(request)
        
        return response
        