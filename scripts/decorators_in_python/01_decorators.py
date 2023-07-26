import numpy as np
from string import ascii_lowercase, ascii_uppercase


def to_uppercase(func_):
    return func_().upper


@to_uppercase
def get_random_string() -> str:
    l_alphabet = list(ascii_lowercase + ascii_uppercase)
    return "".join(np.random.choice(l_alphabet, replace=True, size=20))


str1 = get_random_string()
print(str1)

