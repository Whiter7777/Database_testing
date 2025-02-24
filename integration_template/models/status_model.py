from pydantic import BaseModel


class StatusModel(BaseModel):
    table_name: str = "status"
    column_name: str = "name"
    name: str = None
