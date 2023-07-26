import datetime as dt
import pandas as pd
import os
from functools import reduce
import numpy as np


def df_load_stooq_time_series_data_from_file(str_file_path: str, str_stock_name: str) -> pd.DataFrame:
    df = pd.read_csv(
        str_file_path,
        date_parser=lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date(),
        parse_dates=["Date"]
    )
    df.rename(
        columns={
            **{el: str_stock_name + "_" + el.lower() for el in list(set(df.columns).difference("Date"))},
            **{"Date": "quote_date"}
        },
        inplace=True
    )
    return df


def df_load_stock_prices_time_series() -> pd.DataFrame:
    str_data_folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    l_str_stocks = ["asseco", "bogdanka", "pekao"]
    dict_file_names = dict(zip(
        l_str_stocks, [el + "_gpw_prices.csv" for el in l_str_stocks]
    ))
    dict_data = {}
    for key, val in dict_file_names.items():
        df_iter = df_load_stooq_time_series_data_from_file(
            str_file_path=os.path.join(str_data_folder_path, val), str_stock_name=key
        )
        dict_data[key] = df_iter
    df = reduce(
        lambda df_l, df_r: pd.merge(df_l, df_r, on="quote_date", how="outer"),
        list(dict_data.values())
    )
    return df


def df_load_strokes_medical_data() -> pd.DataFrame:
    """
    Data set fetched from Kaggle: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
    I do not own the data.
    """
    str_path_to_data_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "healthcare-dataset-stroke-data.csv")
    df = pd.read_csv(str_path_to_data_file, na_values=[np.nan, "Unknown"])
    df.dropna(subset=["bmi", "smoking_status"], inplace=True)
    df.drop(columns=["id"], inplace=True)
    df.columns = [el.lower() for el in list(df.columns)]
    return df
