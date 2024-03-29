# this note is based on the text: https://www.datacamp.com/tutorial/usage-asterisks-python

# ============================================================================================================
# ========================================== UNPACKING ITERABLES =============================================
# unpacking lists
list1 = [1, 3, 2, 5]
a, *b, c = list1
print(a, b, c)
# unpacking tuples
tuple1 = ("a", "b", "c", "d", "e")
arg1, *l_arg, arg2 = tuple1
print(arg1, l_arg, arg2)
# unpacking sets
set1 = {3, 1, 2, 10, 333, 11}
x, *y, z = set1
print(x, y, z)
# ============================================================================================================


# ============================================================================================================
# ========================================== COMBINING ITERABLES =============================================
l2 = [1, 2, 3]
t2 = (4, 5, 6)
s2 = {7, 8, 9}
cb_l = [*l2, *t2, *s2]
cb_t = (*l2, *t2, *s2)
cb_s = {*l2, *t2, *s2}
# ============================================================================================================


# ============================================================================================================
# ========================================== NESTED UNPACKING ================================================
my_words_list = ["qwerty", "asdf", "zxcv"]
[a, *b], *c = my_words_list
# ============================================================================================================


# ============================================================================================================
# ======================================= CONCATENATING DICTS ================================================
dict1 = {"a": 12, "b": 33}
dict2 = {"c": 33, "a": 1234}
dict3 = {**dict1, **dict2}
# ============================================================================================================


# ============================================================================================================
# ======================================= ARGS in functions ==================================================
def sum_elements(*args):
    return sum(args)


my_args = [1, 3, 2]
sum_elements(*my_args)
# ============================================================================================================

