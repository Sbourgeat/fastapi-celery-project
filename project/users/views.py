# project/users/views.py

import logging
import random
from string import ascii_lowercase

import requests
from celery.result import AsyncResult
from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import users_router
from .schemas import UserBody
from .tasks import sample_task, task_process_notification, task_send_welcome_email
from .models import User
from project.database import get_db_session


logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="project/users/templates")


def api_call(email: str):
    if random.choice([0,1]):
        raise Exception("random processing error")
    
    requests.post("https://httpbin.org/delay/5")


@users_router.get("/form/")
def form_example_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@users_router.post("/form/")
def form_example_post(user_body: UserBody):
    task = sample_task.delay(user_body.email)
    return JSONResponse({"task_id": task.task_id})


@users_router.get("/task_status/")
def tast_status(task_id: str):
    task = AsyncResult(task_id)
    state = task.state

    if state == 'FAILURE':
        error = str(task.result)
        response = {
            'state':state,
            'error':error,
        }
    else:
        response = {
            'state': state,
        }
    return JSONResponse(response)


@users_router.post("/webhook_test/")
def webhook_test():
    if not random.choice([0,1]):
        raise Exception()
    

    requests.post("https://httpbin.org/delay/5")
    return "pong"


@users_router.post("/webhook_test_async/")
def webhook_test_async():
    task = task_process_notification.delay()
    print(task.id)
    return "pong"


@users_router.get("/form_ws/")
def form_ws_example(request: Request):
    return templates.TemplateResponse("form_ws.html", {"request": request})


@users_router.get("/transaction_celery/")
def transaction_celery(session: Session = Depends(get_db_session)):
    username = random_username()
    user = User(
        username=f"{username}",
        email=f"{username}@gmail.com",
    )
    with session.begin():
        session.add(user)
    
    logger.info(f"user {user.id} {user.username} is persistent now")
    task_send_welcome_email.delay(user.id)
    return {"message": "done"}


def random_username():
    username = "".join([random.choice(ascii_lowercase) for _ in range(5)])
    return username
