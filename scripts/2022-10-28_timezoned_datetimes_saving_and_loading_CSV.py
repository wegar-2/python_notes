import datetime as dt
import pandas as pd
import numpy as np
import os
import pytz

CET = pytz.timezone("CET")
UTC = pytz.UTC

dt_start = pd.to_datetime(dt.datetime(2022, 10, 1)).tz_localize(CET)
dt_end = pd.to_datetime(dt.datetime(2022, 10, 1, hour=23, minute=30)).tz_localize(CET)

df = pd.DataFrame(data={
    "my_datetime": pd.date_range(start=dt_start, end=dt_end, freq="1H"),
})
df["var_X"] = np.random.normal(size=df.shape[0])

# save
df.to_csv(
    "temp.csv", index=False, date_format="%Y-%m-%dT%H:%M:%SZ%z"
)

# load
df_rl = pd.read_csv(
    "temp.csv", parse_dates=["my_datetime"],
    date_parser=lambda x: pd.to_datetime(dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ%z")).astimezone(tz=CET),
    dtype={
        "var_X": np.float32
    }
)
df_rl["my_datetime"][0]
