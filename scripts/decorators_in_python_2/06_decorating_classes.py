# Topics: staticmethod, classmethod, property decorators


class Point2d:

    def __init__(self, x, y):
        self.x_ = x
        self.y_ = y

    def __repr__(self):
        return f"this 2d point has coordinates: ({self.x}, {self.y})"

    @property
    def x(self):
        return self.x_

    @x.setter
    def x(self, x):
        self.x_ = x

    @property
    def y(self):
        return self.y_

    @y.setter
    def y(self, y):
        self.y_ = y


point_ = Point2d(1.1, 3.22)
print(repr(point_))

point_.x = 100*point_.x
point_.y = 100*point_.y
print(repr(point_))
