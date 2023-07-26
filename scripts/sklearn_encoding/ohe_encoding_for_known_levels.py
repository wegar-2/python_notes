import numpy as np
from sklearn.preprocessing import OneHotEncoder

# note: when doing one-hot encoding on the ar2, the encoder has to know that there are 3 levels!
l_str_levels = ["a", "b", "c"]
ar1 = np.array(["a", "a", "b", "c", "b", "b", "c"]).reshape(-1, 1)
ar2 = np.array(["a", "a", "b"]).reshape(-1, 1)

# work with encoder: only ar1 (categories="auto" is the default, here it is written out explicitly)
ohe1 = OneHotEncoder(categories="auto")
ohe1.fit(ar1)
ar1_encoded = ohe1.transform(ar1).toarray()
print(ar1)
print(ar1_encoded)

# using the encoder incorrectly: fitting the encoder to ar2 does not account for the fact that there
# is one more level allowed: "c"
ohe_incorrect = OneHotEncoder(categories="auto")
ohe_incorrect.fit(ar2)
ar2_encoded = ohe_incorrect.transform(ar2).toarray()
print(ar2_encoded)

# using the encoder correctly
ohe_correct = OneHotEncoder(categories=[["a", "b", "c"]])
ohe_correct.fit(ar2)
ar2_encoded_correctly = ohe_correct.transform(ar2).toarray()
print(ar2_encoded_correctly)
# Note:there is a third column of zeros in ar2_encoded_correctly
