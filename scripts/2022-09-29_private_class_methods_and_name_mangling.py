import numpy as np
import typing as t

# =============================
# ===== TABLE OF CONTENTS =====
# 1. PRIVATE METHODS      =====
# 2. NAME MANGLING        =====
# 3. SOURCES              =====
# =============================


class Point2D:

    def __init__(self):
        self.x, self.y = np.random.normal(0, 100, 2)

    def _get_coords(self) -> t.Tuple[float, float]:
        return self.x, self.y

    def __get_coords(self) -> t.Tuple[float, float]:
        return self._get_coords()


# ========== 1. PRIVATE METHODS ==========
# Private method convention in Python: its name starts with a single underscore;
# method _get_coords in the class Point2D above is a private method.
# Note: privacy is NOT enforced in Python, hence the calling the private method will not result in an error,
# although Pycharm complains about accessing it by highlighting the call
my_point = Point2D()
print(my_point._get_coords())


# ========== 2. NAME MANGLING ==========
# Now, try to access the other Point2D method prefixed with dunder, i.e. __get_coords:
my_point.__get_coords()

# This throws the following error:
# AttributeError: 'Point2D' object has no attribute '__get_coords'. Did you mean: '_get_coords'?

# Looking and the attributes and methods of my_ponint...
for i, el in enumerate(dir(my_point)):
    print(i, ": ", el)

#This prints (truncated):
# 0 :  _Point2D__get_coords
# 1 :  __class__
# 2 :  __delattr__
# 3 :  __dict__
# ...........
#
# Conclusion: although my_point does not have method __get_coords it seems to have method _Point2D__get_coords!
print(my_point._Point2D__get_coords())

# This call prints:
# (20.22377678801885, -125.05887700662677)
# although PyCharm complains about making this call

# Name mangling is best considered with inheritance. Consider the following two classes:
# RectangularMatrix (parent class) and SquareMatrix (child class)


class RectangularMatrix:

    def __init__(self, m: int = 2, n: int = 3):
        self.data = np.random.normal(0, 100, size=(m, n))

    def __print_element(self, i_: int, j_: int):
        print("Element (", i_, ", ", j_, ") of this RECTANGULAR matrix is: ", self.data[i_, j_])

    def square_all_elements(self):
        self.data = self.data ** 2


class SquareMatrix(RectangularMatrix):

    def __init__(self, n):
        super().__init__(n, n)

    def __print_element(self, i_: int, j_: int):
        print("Element (", i_, ", ", j_, ") of this SQUARE matrix is: ", self.data[i_, j_])

    def square_all_elements(self):
        print("Squaring all elements of this square matrix...")
        super().square_all_elements()


square_matrix = SquareMatrix(3)

for i, el in enumerate(dir(square_matrix)):
    print(i, ": ", el)

# Output is:
# 0 :  _RectangularMatrix__print_element
# 1 :  _SquareMatrix__print_element
# 2 :  __class__
# 3 :  __delattr__
# ...........

# ========== 3. SOURCES ==========
# 1. Python docs:
#     https://docs.python.org/3/tutorial/classes.html#private-variables
# 2. A StackOverflow discussion:
#     https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
# 3. An article:
#     https://codefather.tech/blog/private-methods-python/
