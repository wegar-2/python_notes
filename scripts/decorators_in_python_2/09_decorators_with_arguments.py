import numpy as np


def my_wrapper():
    pass


def my_test_function(N):
    ar_ = np.random.randint(1, 21, N)
    print(f"Generated random numbers: {ar_}")
    return np.sum(ar_)

