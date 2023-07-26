import numpy as np


def print_log_decorator(fn_):
    def wrapper():
        print(f"Starting execution of {fn_.__name__}...")
        fn_()
        print(f"Completed execution of {fn_.__name__}! ")
    return wrapper


@print_log_decorator
def my_test_fun():
    m_ = np.random.randint(-101, 100, size=(3, 5))
    print(m_)
    return m_


my_test_fun()
