import numpy as np


# 1. simplest decorator --- of a function that takes in no arguments
def my_decor1(fn_):
    def wrapper_():
        print(f"calling function {fn_.__name__}...")
        fn_()
        print(f"successfully called function {fn_.__name__}!")
    return wrapper_


@my_decor1
def print_some_numbers():
    print(f"Some random numbers: {np.random.randint(1, 11, 5)}")


print_some_numbers()


# 2. wrapping function that takes in arguments and returns output


def my_decor2(fn_):
    def wrapper(*args, **kwargs):
        fn_(*args, **kwargs)
        return fn_(*args, **kwargs)
    return wrapper


@my_decor2
def print_n_random_numbers(N: int):
    ar = np.random.randint(1, 101, N)
    print(f"My array is: \n{ar}")
    return ar


print(print_n_random_numbers(20))


