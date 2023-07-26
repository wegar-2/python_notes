import tensorflow as tf
import numpy as np

# 1. addition of two tensorflow tensors
t1 = tf.ones((5, 1))
t2 = tf.random.normal(shape=(5, 1))
print((t1 + t2).numpy())

# 2. subtraction of tensors
t3 = tf.random.normal(shape=(3, 4))
t4 = tf.random.normal(shape=(3, 4))
t5 = t4 - t3

# 3. multiplication of all elements of tensor by a number
const_tens = tf.constant(3)
t6 = tf.convert_to_tensor(np.arange(1, 5, 1))
t7 = tf.reshape(t6, shape=(2, 2))
print(tf.multiply(2, t7))
print(tf.multiply(const_tens.numpy(), t7))
