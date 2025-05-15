# project/users/__init__.py

from fastapi import APIRouter

users_router = APIRouter(
    prefix="/users",
)

from . import views, models, tasks # noqa
