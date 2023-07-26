

my_number = 0b1010
my_string = "0b0100"

print(my_number)
my_number2 = int(my_string[2:], 2)
print(my_number2)


#   pre-underscore, e.g. _x: used for private class variables
#   post-underscore, e.g. int_: used for avoiding collisions with keywords when naming variables
#   double pre-underscore: __x: used for handling name mangling
