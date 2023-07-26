import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os

str_data_folder_path = os.path.join(os.path.dirname(__file__), "..", "..", "data")

# load the data
l_cols = ["Date", "Close"]
df_lwb = pd.read_csv(os.path.join(str_data_folder_path, "bogdanka_gpw_prices.csv"))
df_lwb = df_lwb[l_cols]
df_lwb.rename(columns={"Close": "bogdanka"}, inplace=True)
df_peo = pd.read_csv(os.path.join(str_data_folder_path, "pekao_gpw_prices.csv"))
df_peo = df_peo[l_cols]
df_peo.rename(columns={"Close": "pekao"}, inplace=True)
df_data = pd.merge(
    left=df_lwb, right=df_peo, left_on="Date", right_on="Date", how="outer"
)
print(df_data.isna().sum(axis=0))

# make simple line plot of prices
df_data.set_index("Date", inplace=True)
df_data.sort_index(axis=0, ascending=True, inplace=True)
df_data["bogdanka"].plot(legend=True, color="blue")
df_data["pekao"].plot(legend=True, color="green", secondary_y=True)
plt.show()

# calculate index of prices
df_ratios = df_data / df_data.iloc[0, :] * 100
df_ratios["bogdanka"].plot(legend=True, color="b")
ax = df_ratios["pekao"].plot(legend=True, secondary_y=False, color="g")
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()

# add 1D lags of prices
df_data_lags = df_data.shift(1).rename(columns=dict(zip(
    df_data.columns, [el + "_lag1d" for el in list(df_data.columns)]
)))
df_data = pd.concat([df_data, df_data_lags], axis=1)
df_data["logret_bogdanka"] = np.log(df_data["bogdanka"] / df_data["bogdanka_lag1d"])
df_data["logret_pekao"] = np.log(df_data["pekao"] / df_data["pekao"].shift(-1))
df_data.plot.scatter(x="logret_bogdanka", y="logret_pekao")
plt.show()

# make plot with simple moving average
df_prices = df_data[["bogdanka"]].copy()
df_prices["bogdanka_sma200"] = df_prices["bogdanka"].rolling(200).mean().copy()
df_prices["bogdanka_sma50"] = df_prices["bogdanka"].rolling(50).mean().copy()
df_prices.plot()
plt.show()
