from pydantic import BaseModel


class AuthorModel(BaseModel):
    name: str
    login: str
    email: str
