import numpy as np


def create_artificial_dataset(
        ar_params: np.array, ar_indeps_limits: np.array, fl_sigma: float, fl_intercept: float,
        int_sample_size: int = 1000):
    # create dictionary with values of independent variables
    dict_of_cols = {
        i: np.random.uniform(low=ar_indeps_limits[i, 0], high=ar_indeps_limits[i, 1], size=int_sample_size).reshape(-1, 1)
        for i in range(len(ar_params))
    }
    X = np.concatenate(list(dict_of_cols.values()), axis=0)
    y = fl_intercept + np.dot(X, ar_params.reshape(-1, 1)) + \
        np.random.normal(loc=0, scale=fl_sigma, size=int_sample_size).reshape(-1, 1)
    return X, y


