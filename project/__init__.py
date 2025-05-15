# project/__init__.py

from contextlib import asynccontextmanager
from broadcaster import Broadcast
from fastapi import FastAPI

from project.celery_utils import create_celery
from project.config import settings


broadcast = Broadcast(settings.WS_MESSAGE_QUEUE)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await broadcast.connect()
    yield
    await broadcast.disconnect()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    from project.logging import configure_logging
    configure_logging()

    # do this before loading routes
    app.celery_app = create_celery()

    from project.users import users_router
    app.include_router(users_router)

    from project.ws import ws_router
    app.include_router(ws_router)


    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    
    return app
