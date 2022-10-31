import math
import itertools

# define a set to work with
set_ = {"a", "A", 1, math.pi}

# get all permutations
l_permutations = list(itertools.permutations(set_))
print(l_permutations)
for num, val in enumerate(l_permutations):
    print(num, ": ", val)

# get all combinations of set_: 2-element subsets of 4-element set
l_combinations = list(itertools.combinations(set_, r=2))
print(l_combinations)
print(len(l_combinations) == math.comb(4, 2))

