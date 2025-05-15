# project/users/schemas.py

from pydantic import BaseModel

class UserBody(BaseModel):

    username: str
    email: str