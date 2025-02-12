from pydantic import BaseModel

class TestUserInterfaceModel(BaseModel):
    timer_start_value: str
    lat_letters_quant_in_range: tuple
    cyr_letters_quant_in_range: tuple
    email_letters_quant_in_range: tuple
    domain_letters_quant_in_range: tuple
    digit_quant_in_range: tuple
    number_selected_checkboxes: int