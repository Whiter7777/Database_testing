from pydantic import BaseModel


class AuthorModel(BaseModel):
    table_name: str = "author"
    column_name: str = "name"
    name: str = None
    login: str = None
    email: str = None
