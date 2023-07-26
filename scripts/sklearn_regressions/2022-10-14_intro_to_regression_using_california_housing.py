import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_validate, GridSearchCV
from sklearn import datasets
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set_theme(style="whitegrid")

# quick look at the data
df_X, df_y = datasets.fetch_california_housing(return_X_y=True, as_frame=True)
print(df_X.describe())
df_y = pd.DataFrame(df_y)
df_y.plot(kind="hist", bins=50)
plt.show()

# import the data as arrays
X, y = datasets.fetch_california_housing(return_X_y=True, as_frame=False)
X_train, X_test, y_train, y_test = train_test_split(X, y)

# fit simple linear regression with cross validation
kf = KFold(n_splits=6)
cross_val_res = cross_validate(LinearRegression(), X, y, cv=kf)

# fit Lasso with various thresholds using GridSearchCV
ar_caps = np.array([0.1, 1, 10, 100, 1000, 10000])
gs_cv = GridSearchCV(estimator=Lasso(), param_grid={"alpha": ar_caps}, cv=kf)
gs_cv.fit(X_train, y_train)
best_estimator = gs_cv.best_estimator_
y_test_hat = best_estimator.predict(X_test)

