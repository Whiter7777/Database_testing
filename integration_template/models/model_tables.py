from pydantic import BaseModel


class AuthorTable(BaseModel):
    table_name: str
    column_name: str


class ProjecrTable(BaseModel):
    table_name: str
    column_name: str


class StatusTable(BaseModel):
    table_name: str
    column_name: str


class SessionTable(BaseModel):
    table_name: str
    column_name: str


class TestTable(BaseModel):
    table_name: str
    column_name: str
    condition: str
