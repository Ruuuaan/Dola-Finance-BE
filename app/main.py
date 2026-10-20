
from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers import goals
from app.db.database import init_db
from app.routers import goals


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(goals.router)
