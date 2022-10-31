import itertools
from string import ascii_uppercase as upal

# Cartesian product of two iterables
import pandas as pd

l_pairs = list(itertools.product(list(upal), (1, 2)))
for el in l_pairs:
    print(el)

# chaining of containers: multiple containers passed as *args
l_final = list(itertools.chain([3, 1, "A"], (3, 4, "q")))
print(l_final)

# chaining of a container of containers
l_final_mc = list(itertools.chain.from_iterable(
    [
        ("1", "t", 32),
        [90, 4,  "q"],
        {2, "qwe", 1},
        {"a": 1, "b": 43}]
))
print(l_final_mc)

# repeating a finite iterable until cet
list(itertools.islice(itertools.cycle(["a", "q", "r"]), 11))
