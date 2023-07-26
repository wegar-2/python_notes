import numpy as np

# get array of numbers from 1 to 18 (inclusive) by 1
nums = np.arange(1, 19, 1)
print(nums.shape)
print(nums)

# reshape the array nums into matrix 2 by 9 row
mr = nums.reshape(2, -1, order="C")
print(mr)

# reshape the array of nums into matrix 3 by 6 by columns
mc = nums.reshape(3, 6, order="F")
print(mc)

# reshape matrix into 1d array ---> concatenate rows
print(mr)
print(mr.flatten(order="C"))

# reshape matrix into 1d array ---> concatenate columns
print(mc)
print(mc.flatten(order="F"))



