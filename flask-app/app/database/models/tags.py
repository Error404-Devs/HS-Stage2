from pydantic import BaseModel
from typing import Union
from app.database.models.users import User

class Tag(BaseModel):
    name: str
    id: str
    data: Union[User, str]
