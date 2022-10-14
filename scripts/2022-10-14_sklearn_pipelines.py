import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

# quick look at the data
df_X, df_y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)
df_y = pd.DataFrame(df_y)
print(df_X.describe())
print(df_y.groupby("target")["target"].count())

# load numerical data + split into test and train data set
X, y = datasets.load_breast_cancer(return_X_y=True, as_frame=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=int(0.2*X.shape[0]))

# create pipeline object
pipe_ = Pipeline([
    ("scaling", StandardScaler()),
    ("fitting", KNeighborsClassifier())
])

# fit a single pipeline using the train data
pipe_.fit(X_train, y_train)
y_test_hat = pipe_.predict(X_test)

