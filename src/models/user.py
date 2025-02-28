from pydantic import BaseModel, constr, Field


class User(BaseModel):
    room: str
    name: constr(min_length=1)
    messages: list = Field(default_factory=list)
