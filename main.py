from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.firebase_service import FirebaseService
from routers import agent, user
from middleware.auth import AuthTokenMiddleWare
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
FirebaseService.init()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(AuthTokenMiddleWare)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(agent.router)
app.include_router(user.router)