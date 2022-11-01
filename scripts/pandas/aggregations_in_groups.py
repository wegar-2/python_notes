import pandas as pd
from utils.package_data_loaders import df_load_stock_prices_time_series
import numpy as np


# load data on stocks prices
df = df_load_stock_prices_time_series()
# fill NAs: forward fill + bfill
df.ffill(axis=0, inplace=True)
df.bfill(axis=0, inplace=True)
# check for NAs
print(df.isna().sum(axis=0))
print(df.dtypes)

# define helper lists for working with data
l_companies = ["asseco", "bogdanka", "pekao"]
l_variables = ["open", "high", "low", "close", "volume"]


# to start with, work with pekao prices only
l_pekao_variables = ["pekao_" + el for el in l_variables]
df_pekao = df[["quote_date"] + l_pekao_variables].copy()

# calculate the same, yearly descriptive statistics for multiple columns at the same time
df_pekao["quote_year"] = df_pekao["quote_date"].dt.year
df_pekao.groupby("quote_year")["quote_date"].count()
df_summaries = df_pekao.groupby("quote_year")[l_pekao_variables].agg([np.min, np.max, np.mean])

# calculate different statistics for different columns
df_customized_summary = df_pekao.groupby("quote_year").agg({
    "pekao_close": [np.min, np.max],
    "pekao_volume": [np.median, np.average]
})

# calculate daily averages of the OHLC prices without grouping
l_ohlc_cols = ["pekao_" + el for el in ["open", "high", "low", "close"]]
df_pekao["ohlc_average"] = df_pekao.apply(lambda x: np.average(x[l_ohlc_cols]), axis=1)

# add column with average close price to every row in the dataset
df_pekao["avg_yearly_close_price"] = df_pekao.groupby("quote_year")["pekao_close"].transform(np.mean)
