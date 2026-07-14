from pydantic import BaseModel
from pydantic import ConfigDict


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int


class StudentUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    age: int

    model_config = ConfigDict(from_attributes=True)