from functools import wraps
import numpy as np


def my_decorator(fn_):
    @wraps(fn_)                                     # NOTE: fn_ is passed to functools.wraps() !!!!!
    def wrapper_(*args, **kwargs):
        print(f"before calling {fn_.__name__}...")
        fn_(*args, **kwargs)
        print(f"after calling {fn_.__name__}...")
    return wrapper_


@my_decorator
def my_test_fun(n: int):
    """
    This function generates 1 dim array of random normally distributed numbers.
    """
    ar = np.random.randn(n)
    return ar


my_test_fun(10)
print(my_test_fun.__doc__)
