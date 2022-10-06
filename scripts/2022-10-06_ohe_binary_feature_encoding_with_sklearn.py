from sklearn.preprocessing import OneHotEncoder
import numpy as np

# set random seed for replicability
np.random.seed(seed=113)

# generate a vector of binary features
ar_bin_feat = np.random.randint(low=0, high=2, size=(100, 1))
print(ar_bin_feat.shape)

# create instance of one-hot encoder
enc = OneHotEncoder()
enc.fit(ar_bin_feat)
print(enc.categories_)
ar_bin_feat_ohe = enc.fit_transform(X=ar_bin_feat).toarray()

print(ar_bin_feat[0:3, ])
print(ar_bin_feat_ohe[0:3, ])

