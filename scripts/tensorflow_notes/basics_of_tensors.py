import tensorflow as tf
import numpy as np

t1 = tf.ones((1, 3))

# 1. nice printing of a tensor
print(t1.numpy())

# 2. casting numpy array as tensor
print(t1)
print(type(t1))
ar0 = np.random.normal(size=(5, 5))
t2 = tf.convert_to_tensor(ar0)
print(t2.numpy())

# 3. reshaping a tensor
ar1 = np.arange(1, 13, 1)
ar1 = np.reshape(ar1, order="F", newshape=(2, 6))
t3 = tf.convert_to_tensor(ar1)
print(t3.numpy())
t4 = tf.reshape(t3, shape=(3, 4))
print(t4.numpy())
t5 = tf.reshape(t3, shape=(-1, 1))
print(t5.numpy())

# 4. what is of class tf.Tensor?
t6 = tf.constant(value=[[1, 2], [3, 4]], shape=(2, 2))
print(t6)
type(t6)
print(t6 is tf.Tensor)
t7 = tf.Variable([[1, 2], [3, 4]], shape=(2, 2))
print(t7 is tf.Tensor)


