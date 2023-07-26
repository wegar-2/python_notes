import os
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# loading the data
str_path_to_data_file = os.path.join(os.getcwd(), "data", "healthcare-dataset-stroke-data.csv")
df = pd.read_csv(str_path_to_data_file, na_values=[np.nan, "Unknown"])
print(df.isna().sum(axis=0))
df.dropna(subset=["bmi", "smoking_status"], inplace=True)
df.drop(columns=["id"], inplace=True)
df.columns = [el.lower() for el in list(df.columns)]
print(df.isna().sum(axis=0))

# summary statistics
print(df.dtypes)
print(df.describe())

# histograms of continuous variables histograms
df["age"].plot.hist()
plt.show()
df["bmi"].plot.hist()
plt.show()
df["avg_glucose_level"].plot.hist()
plt.show()

# bar charts of categortical / binary variables
df["hypertension"].plot.bar()
plt.show()

#