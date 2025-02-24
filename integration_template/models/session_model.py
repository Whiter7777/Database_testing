from pydantic import BaseModel, field_serializer
import datetime


class SessionModel(BaseModel):
    table_name: str = "session"
    column_name: str = "session_key"
    session_key: str = None
    created_time: datetime.datetime = None
    build_number: int = None

    @field_serializer('created_time')
    def serialize_dt(self, created_time: datetime, _info):
        return created_time.timestamp()
