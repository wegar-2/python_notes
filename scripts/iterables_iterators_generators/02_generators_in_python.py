# URL: https://www.datacamp.com/tutorial/python-iterators-generators-tutorial


# The yield keyword controls the flow of a generator function. Instead of exiting the function as seen when
# return is used, the yield keyword returns the function but remembers the state of its local variables.

def get_next_multiple_of_number(num: int):
    mult = 1
    while True:
        out = mult*num
        mult += 1
        yield out


my_multiplier_of_three = get_next_multiple_of_number(num=3)
print(next(my_multiplier_of_three))
print(next(my_multiplier_of_three))
print(next(my_multiplier_of_three))

