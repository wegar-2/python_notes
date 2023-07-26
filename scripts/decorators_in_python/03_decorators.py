import numpy as np


def increase_by_eleven(func_):
    def internal_(arg1, arg2):
        return func_(arg1, arg2) + 11
    return internal_


@increase_by_eleven
def sum_of_matrix_elements(n_row: int, n_col: int):
    m1 = np.random.randint(-100, 101, n_row*n_col).reshape((n_row, n_col))
    print(m1)
    return np.sum(m1)


print(sum_of_matrix_elements(3, 5))
