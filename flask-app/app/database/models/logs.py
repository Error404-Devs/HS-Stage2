import datetime
from pydantic import BaseModel
from app.database.models.tags import Tag

class Log(BaseModel):
    message: str
    id: str
    tag: Tag
    date_logged: datetime.datetime
