from pydantic import BaseModel
from integration_template.models.author_model import AuthorModel
from integration_template.models.project_model import ProjectModel


class ConfigModel(BaseModel):
    startUrl: str
    env: str
    project: ProjectModel
    session: str
    author: AuthorModel
