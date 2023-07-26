import numpy as np


def my_decorator(fn_):
    def wrapper(*args):
        print(f"Starting execution of {fn_.__name__}...")
        fn_(*args)
        print(f"Completed execution of {fn_.__name__}! ")
    return wrapper


@my_decorator
def print_random_numbers(how_many: int):
    for i in range(how_many):
        print(f"{i}-th random integer from range [1, 1000]: {np.random.randint(1, 1001)}...")


print_random_numbers(5)
