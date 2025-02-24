from pydantic import BaseModel, field_serializer
import datetime


class TestModel(BaseModel):
    table_name: str = "test"
    column_name: str = "status_id"
    condition: str = "id"
    name: str = None
    status_id: int = None
    method_name: str = None
    project_id: int = None
    session_id: int = None
    start_time: datetime.datetime = None
    end_time: datetime.datetime = None
    env: str = None
    browser: str = None
    author_id: int = None

    @field_serializer('start_time')
    def serialize_dt(self, start_time: datetime, _info):
        return start_time.timestamp()

    @field_serializer('end_time')
    def serialize_dt(self, end_time: datetime, _info):
        return end_time.timestamp()
