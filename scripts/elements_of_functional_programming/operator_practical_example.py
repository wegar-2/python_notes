from operator import itemgetter
import string
import numpy as np

# USECASE: suppose you are working with a big dictionary (i.e. dictionary with large number of entries) and
# you need to access multiple elements of the dictionary

l_alphabet = list(string.ascii_uppercase)
dict_ = dict(zip(
    l_alphabet, list(map(lambda x: x**3 + x**2, list(range(1, len(l_alphabet) + 1, 1))))
))

print("Printing out the dictionary dict_: ")
for key, val in dict_.items():
    print(key, ": ", val)

np.random.seed(12345)
l_keys = list(np.random.choice(l_alphabet, size=10, replace=True))
l_values = list(itemgetter(*l_keys)(dict_))
print("keys: ", l_keys)
print("values: ", l_values)


# ======================================================================================================================
# alternatively, multiple elements of a dictionary can be fetched using list comprehension
l_vals_other = [dict_[el] for el in l_keys]
print(l_vals_other == l_values)
