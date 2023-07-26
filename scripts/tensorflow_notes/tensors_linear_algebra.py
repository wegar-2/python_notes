import tensorflow as tf
import numpy as np

# prepare matrices
t1 = tf.convert_to_tensor(np.arange(1, 13, 1).reshape((3, 4)))
t2 = tf.convert_to_tensor(np.arange(13, 25, 1).reshape((3, 4)))
t3 = tf.convert_to_tensor(np.arange(25, 37, 1).reshape((4, 3)))

# Hadamard multiplication
print(tf.multiply(t1, t2))

# standard matrix multiplication (m, n) x (n, k) ===> (m, k)
print(tf.matmul(t3, t1))
print(tf.matmul(t2, t3))

# using .reduce_sum() method
print(t1)
# calculating column sums
print(tf.reduce_sum(t1, axis=0).numpy())
# calculating rowsums
print(tf.reduce_sum(t1, axis=1, keepdims=True).numpy())
