import numpy as np
from sklearn.preprocessing import OneHotEncoder
from string import ascii_uppercase

# set seed
np.random.seed(1133)

# generate categorical data
my_categs = list(ascii_uppercase[0:5])
print(my_categs)

# prepare column vector of categorical data
ar_categs = np.random.choice(my_categs, size=(100, 1), replace=True)

# create an OHE encoder instance: note that the categories are NOT given in alphabetical order
enc = OneHotEncoder(categories=[["C", "D", "B", "A", "E"]])
ar_categs_encoded = enc.fit_transform(X=ar_categs).toarray()

# note that the columns are filled with ones from left to right acc. to the order defined during the initalization
# of the encoder
print(ar_categs[1:7, :])
print(ar_categs_encoded[1:7, :])

