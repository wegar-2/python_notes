import numpy as np


def logger_dec():
    pass


def doubler_decorator(fn_):
    def wrapper_(*args, **kwargs):
        fn_(*args, **kwargs)            # first call
        return fn_(*args, **kwargs)     # second call + returning the value
    return wrapper_


def print_some_numbers_one(n):
    print(f"Some random numbers from inside {print_some_numbers_one.__name__}: {np.random.randn(n)}")


def print_some_numbers_two(n):
    print(f"Some random numbers from inside {print_some_numbers_one.__name__}: {np.random.randn(n)}")


print_some_numbers_one(10)
print_some_numbers_two(3)

