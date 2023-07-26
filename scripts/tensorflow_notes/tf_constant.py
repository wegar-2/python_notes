import numpy as np
import tensorflow as tf

# creating instance of tf.constant
t1 = tf.constant(np.arange(1, 5, 1), shape=(4, 1))
print(t1)
print(type(t1))
print(t1[1:3, 0])

# The line below cannot be executed: tensorflow does not support modification of tf.constant instaces
# t1[1, 0] = 111

ar1 = np.random.normal(size=(4, 3))
t1 = tf.convert_to_tensor(ar1)
print(type(t1))
print(t1.numpy())
# t1[1, 2] = 1234