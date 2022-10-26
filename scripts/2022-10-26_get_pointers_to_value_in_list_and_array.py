import numpy as np

my_list = [1, 4, 1, 7, 9, 10, 1, 3, 5]
print(my_list.index(7))
print(my_list.index(1))

# get positions of a value in a list
list_locations = [p for p, v in enumerate(my_list) if v == 1]
print(list_locations)

# get position in 1-dim array
np.random.seed(seed=12345)
ar = np.random.normal(loc=10, scale=5, size=10)
ar = np.round(ar, 2)
print(ar)
print(np.where(ar == 7.4)[0][0])

# get position(s) of a value in 2-dim array
ar_ints = np.random.randint(low=1, high=6, size=(4, 7))
print(ar_ints)
ar_rp, ar_cp = np.where(ar_ints == 3)
for i in range(len(ar_rp)):
    print(ar_ints[ar_rp[i], ar_cp[i]])

