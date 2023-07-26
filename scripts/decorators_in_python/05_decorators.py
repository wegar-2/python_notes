import numpy as np


def my_decorator(fn):

    def internal_(*args, **kwargs):
        print("asdf")
        res = fn(*args, **kwargs)
        print(f"my sum = {np.sum(res)}")

    return internal_


@my_decorator
def my_matrix_function(n_row: int, n_col: int):
    m_ = np.random.randint(-100, 101, n_row*n_col).reshape((n_row, n_col))
    print(m_)
    return m_


my_matrix_function(5, 9)

