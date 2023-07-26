import numpy as np
from numpy.random import normal


class ParentRng:

    def __init__(self, dim_: int):
        self.dim_ = dim_

    def generate(self):
        return normal(size=self.dim_)


class ChildRng(ParentRng):

    def __init__(self, dim_: int):
        super(ChildRng, self).__init__(dim_=dim_)

    def generate(self):
        return normal(size=(self.dim_, self.dim_))


def my_fun(rng_: ParentRng):
    return rng_.generate()


p_rng = ParentRng(dim_=3)
# print(p_rng.generate())
print(my_fun(p_rng))

# instance of the child class can be passed to the function that accepts
ch_rng = ChildRng(dim_=3)
# print(ch_rng.generate())
print(my_fun(ch_rng))




