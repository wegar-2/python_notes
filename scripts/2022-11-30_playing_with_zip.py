from string import ascii_uppercase
import numpy as np

# https://stackoverflow.com/questions/19339/transpose-unzip-function-inverse-of-zip

l_str_letters = list(ascii_uppercase)
l_numbers = [round(el, 2) for el in np.random.normal(size=len(l_str_letters))]
list_of_tuples = list(zip(l_str_letters, l_numbers))
l_str_letters_retrieved, l_numbers_retreived = list(map(
    lambda x: list(x),
    list(zip(*list_of_tuples))
))
