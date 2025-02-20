import random
from string import ascii_letters
from integration_template.configurations.testing_data_configuration import TestDataConfiguration
from selenium.common.exceptions import InvalidArgumentException


class GetRandomData:
    @staticmethod
    def generate_password(lat_num_min_max: tuple[int, int],
                          cyr_num_min_max: tuple[int, int],
                          digit_num_min_max: tuple[int, int]
                          ):
        cyrillic_lower = [(lambda c: chr(c))(i) for i in range(1072, 1104)]
        cyrillic_upper = [(lambda c: chr(c))(i) for i in range(1040, 1072)]
        cyrillic_ansi = cyrillic_lower + cyrillic_upper
        part_lat = "".join(random.choice(ascii_letters) for i in range(
            random.randint(lat_num_min_max[0], lat_num_min_max[1])))
        part_cyr = "".join(random.choice(cyrillic_ansi) for i in range(
            random.randint(cyr_num_min_max[0], cyr_num_min_max[1])))
        part_num = str(random.randint(digit_num_min_max[0], digit_num_min_max[1]))
        return (part_lat+part_cyr+part_num).title()

    @staticmethod
    def generate_random_numbers(range_list: int, num_of_select: int) -> list:
        if num_of_select <= range_list:
            numbers = list(range(range_list))
            selected_numbers = random.sample(list(numbers), k=num_of_select)
            return selected_numbers
        else:
            raise InvalidArgumentException(
                "Число выбранных элементов должно быть меньше или равным количеству всех элементов")

    @staticmethod
    def generate_random_text(num_min_max: tuple[int, int]):
        return "".join(random.choice(ascii_letters) for i in range(
            random.randint(num_min_max[0], num_min_max[1])))

    @staticmethod
    def generate_random_number(num_min_max: tuple[int, int]):
        return random.randint(num_min_max[0], num_min_max[1])
