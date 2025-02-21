from pydantic import BaseModel
from integration_template.models.model_tables import AuthorTable, ProjecrTable, StatusTable, SessionTable, TestTable


class TestUserInterfaceModel(BaseModel):
    timer_start_value: str
    lat_letters_quant_in_range: tuple
    cyr_letters_quant_in_range: tuple
    email_letters_quant_in_range: tuple
    domain_letters_quant_in_range: tuple
    digit_quant_in_range: tuple
    number_selected_checkboxes: int
    limit: int
    author_table: AuthorTable
    project_table: ProjecrTable
    status_table: StatusTable
    session_table: SessionTable
    test_table: TestTable
