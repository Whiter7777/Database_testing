import random
from string import ascii_letters
from integration_template.configurations.test_data_configuration import TestDataConfiguration


class PasswordGenerator:
    @staticmethod
    def generate_password():
        cyrillic_lower = [(lambda c: chr(c))(i) for i in range(1072, 1104)]
        cyrillic_upper = [(lambda c: chr(c))(i) for i in range(1040, 1072)]
        cyrillic_ansi = cyrillic_lower + cyrillic_upper
        part_lat = "".join(random.choice(ascii_letters) for i in range(random.randint(3, 5)))
        part_cyr = "".join(random.choice(cyrillic_ansi) for i in range(random.randint(3, 5)))
        part_num = str(random.randint(1, 9))
        return (part_lat+part_cyr+part_num+TestDataConfiguration().get_email()).title()
