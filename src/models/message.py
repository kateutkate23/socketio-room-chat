from pydantic import BaseModel, constr


class Message(BaseModel):
    text: constr(min_length=1)
    author: str
