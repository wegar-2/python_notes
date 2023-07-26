import itertools
import functools

# Three core Python higher-order functions are:
#   1) map
#   2) filter
#   3) functools.reduce / itertools.accumulate
#   4) interesting variation on map function: itertools.starmap


# Ad. 1):
print(list(map(lambda x: str(x) + "_qwerty", [1, 3, 12, "ret"])))

# Ad. 2):
print(list(filter(lambda x: len(x) > 3, [[12345], ["q", "t"], (1, 4, 2, 3)])))

# Ad. 3):
print(functools.reduce(lambda x, y: x**2 + x*y + y**2, [1, 3, 2]))

# Ad. 4): sample application of itertools.starmap: calculate value of two-variables function on a grid of pairs of arguments
l_grid_of_pairs = list(itertools.product([1, 2, 3], [1, 2, 3]))
print(list(itertools.starmap(lambda x, y: x**2 + y**2, l_grid_of_pairs)))
