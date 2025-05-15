# project/ws/__init__.py

from fastapi import APIRouter

ws_router = APIRouter()

from . import views # noqa