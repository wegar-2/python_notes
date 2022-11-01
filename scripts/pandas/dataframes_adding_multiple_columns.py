import pandas as pd
from utils.package_data_loaders import df_load_stock_prices_time_series
from itertools import product
import numpy as np


# load data on stocks prices
df = df_load_stock_prices_time_series()

# fill NAs: forward fill + bfill
df.ffill(axis=0, inplace=True)
df.bfill(axis=0, inplace=True)

# check for NAs
print(df.isna().sum(axis=0))

# define helper columns for working with data
l_variables = ["open", "low", "high", "close", "volume"]
l_companies = ["asseco", "bogdanka", "pekao"]
l_value_cols = [el[0] + "_" + el[1] for el in product(l_companies, l_variables)]

# add first order lags and leads to all pekao columns using .assign() method
l_pekao_cols = ["pekao_" + el for el in l_variables]
df = df.assign(**{
    col + "_lag1": df[col].shift(1)
    for col in l_pekao_cols
})

# calculate log-return for OHLC prices of pekao
l_prices_cols = list(set(l_pekao_cols).difference({"pekao_volume"}))
df = df.assign(**{
    "log_return_" + el: np.log(df[el] / df[el + "_lag1"])
    for el in l_prices_cols
})

