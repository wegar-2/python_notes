# URL: https://realpython.com/python-getter-setter/#getting-to-know-getter-and-setter-methods
# getter --> aka accessor
# setter ---> aka mutator
# getter / setter =====> accessor / mutator

class MyPoint:

    def __init__(self, x, y):
        self.x_ = x
        self.y_ = y

    @property
    def x(self):
        print("x coord getter called...")
        return self.x_

    @x.setter
    def x(self, x):
        print("x coord setter called...")
        self.x_ = x

    @property
    def y(self):
        print("y coord getter called...")
        return self.y_

    @y.setter
    def y(self, y):
        print("y coord setter called...")
        self.y_ = y

    def __repr__(self):
        return f"Point with coords ({self.x_}, {self.y_})"


obj_ = MyPoint(21.2, 321)
print(repr(obj_))

obj_.x = 1
obj_.y = 2
print(repr(obj_))
print(f"x: {obj_.x}")
print(f"y: {obj_.y}")

