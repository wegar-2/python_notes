import os
import pandas as pd
import numpy as np

print(os.getcwd())

df = pd.read_csv(
    os.path.join(os.getcwd(), "data", "eurpln_d.csv")
)
df["Close_lag1"] = df["Close"].shift(1)
df["Close_logret"] = df.apply(lambda x: np.log(x["Close"] / x["Close_lag1"]), axis=1)
df["Close_logret_std"] = df["Close_logret"].rolling(window=61).std()

