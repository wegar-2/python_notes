from functools import partial


def add_two_numbers(x, y):
    return x + y


add_ten_to_number = partial(add_two_numbers, y=10)

print(add_ten_to_number(21))
