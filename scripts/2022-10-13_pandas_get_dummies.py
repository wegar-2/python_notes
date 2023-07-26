import pandas as pd
import datetime as dt

date_start = dt.date(year=2021, month=1, day=1)
date_end = dt.date(year=2021, month=12, day=31)

df = pd.DataFrame(
    data={
        "day": pd.date_range(date_start, date_end, freq="D")
    }
)
df["day"] = df["day"].apply(lambda x: x.to_pydatetime().date())
df["day_of_week"] = [el.isoweekday() for el in df["day"]]
df.set_index("day", inplace=True)
df_dummies = pd.get_dummies(data=df["day_of_week"], prefix="weekday")
