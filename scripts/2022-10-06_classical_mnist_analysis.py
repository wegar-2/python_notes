import numpy as np
from keras.datasets import mnist
from sklearn.preprocessing import OneHotEncoder
from keras import Sequential
from keras.layers import Dense, Input


# 1. load the data
(ar_train_indep, ar_train_labels), (ar_test_indep, ar_test_labels) = mnist.load_data()
print(ar_train_indep.shape)
print(ar_test_indep.shape)

# 2. reshape arrays with independent variables
ar_train_indep = ar_train_indep.reshape(60000, 28**2)
ar_test_indep = ar_test_indep.reshape(10000, 28**2)
print(np.min(ar_train_indep))
print(np.max(ar_train_indep))

# 3. scale the independent variables of the test set to the range (0, 1)
ar_train_indep = ar_train_indep / 255
ar_test_indep = ar_test_indep / 255

# 4. do one-hot encoding of dependent variables
ohe_encoder = OneHotEncoder()
ar_train_labels = ohe_encoder.fit_transform(ar_train_labels.reshape(-1, 1)).toarray()
ar_test_labels = ohe_encoder.fit_transform(ar_test_labels.reshape(-1, 1)).toarray()
print(ar_train_labels.shape)
print(ar_test_labels.shape)

# 5. create and compile the network
# create a neural network with three hidden layers 20, 15, 15
network = Sequential(layers=[
    Input(shape=28**2),
    Dense(units=20, activation="relu"),
    Dense(units=15, activation="relu"),
    Dense(units=15, activation="relu"),
    Dense(units=10, activation="softmax")
])
# compile the network, setting the fitting parameters
network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics="accuracy")

# 6. fit the network
network.fit(x=ar_train_indep, y=ar_train_labels, batch_size=128, epochs=7)

# 7. evaluate network fit quality
eval_result = network.evaluate(x=ar_test_indep, y=ar_test_labels)


