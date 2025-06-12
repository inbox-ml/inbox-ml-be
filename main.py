from fastapi import FastAPI
from routers import agent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(agent.router)