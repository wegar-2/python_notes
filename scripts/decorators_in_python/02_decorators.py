import numpy as np


def add_ten(func_in):

    def internal_():
        return func_in() + 10

    return internal_


@add_ten
def get_random_numer():
    out = np.random.normal(loc=1000, scale=1000, size=1)
    print(f"Inside get_random_numer: {out}...")
    return out


print(get_random_numer())


