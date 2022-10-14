import numpy as np
from keras.datasets import mnist
from keras import Sequential
from keras.layers import Input, Dense

# 1. load & format the data
(ar_train_indep, ar_train_labels), (ar_test_indep, ar_test_labels) = mnist.load_data()


# 2. define function for building a network
def make_seq_network():
    pass
