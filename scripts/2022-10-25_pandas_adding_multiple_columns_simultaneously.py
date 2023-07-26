import os
import pandas as pd
import datetime as dt


# df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "pekao_gpw_prices.csv"))
df = pd.read_csv(
    os.path.join(os.getcwd(), "data", "pekao_gpw_prices.csv"),
    parse_dates=["Date"],
    date_parser=lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date()
)

# add up to three lags of each columns other than "Date"
l_cols = list(set(df.columns).difference({"Date"}))
df.apply(lambda x: x[iter_col].shift(iter_lag) for iter_col in l_cols for iter_lag in range(3))
