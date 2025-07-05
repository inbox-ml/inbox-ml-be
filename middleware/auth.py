from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthTokenMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
            return await call_next(request)

        token = request.headers.get("Authorization")
        if token is None or not token.startswith("Bearer"):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

        request.state.token = token.split(" ")[1]
        response = await call_next(request)
        
        return response
        