from pydantic import BaseModel, Field
from typing import Literal


class User(BaseModel):
    id: str
    username: str
    password: str
    role: Literal["Admin", "User"] = "User"