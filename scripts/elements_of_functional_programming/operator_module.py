import operator
import numpy as np

# multiplying respective lists elements
l_1 = [el for el in range(1, 6, 1)]
l_2 = [el**2 for el in range(1, 6, 1)]
print(l_1)
print(l_2)
l_3 = list(map(operator.mul, l_1, l_2))
print(l_3)

# the same can be achieved using numpy arrays
l_3_np = list(np.array(l_1)*np.array(l_2))
print(l_3_np)
