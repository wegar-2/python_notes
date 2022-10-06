import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split, KFold, cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, make_scorer


# load the data to use
# str_datafile_path = "/Users/arturwegrzyn/github_repos/python_notes/data/linear_regression_artificial_data.csv"
str_datafile_path ="..."
df = pd.read_csv(str_datafile_path, index_col=0)
X = df[["X" + str(i) for i in range(1, 4, 1)]].values
y = df["y"].values

# split the data into train and test datasets
train_pctg = 0.8
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=round(train_pctg*y.shape[0]))
print(X_train.shape)
print(X_test.shape)

# create instance of LinearRegrssion
linreg = LinearRegression()

# do the cross validation using R-Squared as the score: cross_val_score function
kf = KFold(n_splits=4)
res_cvs = cross_val_score(
    estimator=linreg,
    scoring=make_scorer(score_func=r2_score, greater_is_better=True),
    cv=kf,
    X=X_train,
    y=y_train
)
print(res_cvs)

# do the cross validation using R-Squared as the score: cross_val_score function
res_cv = cross_validate(
    estimator=linreg,
    X=X_train, y=y_train,
    scoring=make_scorer(score_func=r2_score, greater_is_better=True),
    cv=kf
)
print(res_cv)
