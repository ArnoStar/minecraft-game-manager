from fastapi import FastAPI

from app.presentation.api.routes.server import router as server_router

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before the start of the app
    yield
    # Before the closing of the app


app = FastAPI(lifespan=lifespan)


app.include_router(server_router)
