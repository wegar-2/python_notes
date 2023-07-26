import sys
import inspect


def get_name_of_this_function():
    return inspect.getouterframes(inspect.currentframe())[1].function

# get_name_of_this_function()


def add(x, y):
    print(f"Inside: {get_name_of_this_function()}")
    return x + y

add(10, 12)

