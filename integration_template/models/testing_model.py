from pydantic import BaseModel

class TestUserInterfaceModel(BaseModel):
    email: str
    domain: str
    timer: str