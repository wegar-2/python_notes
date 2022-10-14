import pandas as pd
import os
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np
import seaborn as sns


str_data_folder_path = os.path.join(os.path.dirname(__file__), "..", "..", "data")

l_cols = ["Date", "Close"]
l_dfs = []
for iter_name in ["bogdanka", "pekao", "asseco"]:
    df = pd.read_csv(os.path.join(str_data_folder_path, iter_name + "_gpw_prices.csv"))
    df = df[l_cols]
    df.rename(columns={"Close": iter_name}, inplace=True)
    l_dfs.append(df)

df = reduce(lambda x, y: pd.merge(left=x, right=y, on="Date", how="outer"), l_dfs)
df.set_index("Date", inplace=True)

