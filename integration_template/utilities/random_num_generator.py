import random


class RandomNumGenerator:
    @staticmethod
    def generate_random_numbers(range_list: int):
        numbers = list(range(range_list))
        selected_numbers = random.sample(list(numbers), k=3)
        return selected_numbers
