import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split, KFold, GridSearchCV


# set plotting theme using seaborn
sns.set_theme(style="whitegrid")

# glance at the data
df_X, df_y = datasets.fetch_california_housing(return_X_y=True, as_frame=True)
print(df_X.describe())
df_y = pd.DataFrame(df_y)
df_y.plot(kind="hist", bins=50)
plt.show()

# load data as numpy arrays & split into train & test
X, y = datasets.fetch_california_housing(return_X_y=True, as_frame=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=int(X.shape[0]*0.8))

# create KFold instance
kf = KFold(n_splits=4)

# ------ RIDGE ------
# step 1: see which order of magnitude of alpha is worth exploring in more detail
gs_cv_ridge = GridSearchCV(estimator=Ridge(), param_grid={"alpha": np.array([0.1, 1, 10, 100, 1000])}, cv=kf)
gs_cv_ridge.fit(X_train, y_train)
print(gs_cv_ridge.best_params_)
# step 2: re-run for even higher alphas
gs_cv_ridge = GridSearchCV(estimator=Ridge(), param_grid={"alpha": np.arange(50, 501, 50)}, cv=kf)
gs_cv_ridge.fit(X_train, y_train)
print(gs_cv_ridge.best_params_)
# step 3: check direct neighbourhood of 100
gs_cv_ridge = GridSearchCV(estimator=Ridge(), param_grid={"alpha": np.arange(50, 151, 5)}, cv=kf)
gs_cv_ridge.fit(X_train, y_train)
print(gs_cv_ridge.best_params_)
best_ridge = gs_cv_ridge.best_estimator_
print(gs_cv_ridge.best_score_)
# use best ridge fit to do predictions and visualize them
y_test_hat = best_ridge.predict(X_test)
plt.scatter(x=y_test, y=y_test_hat, alpha=0.7, color="red", s=5, marker="o")
plt.xlabel("actual values")
plt.ylabel("predicted values")
plt.title("Plot of predicted vs actual for best regularization strength parameter value")
plt.show()


# ------- LASSO -------
# step 1
gs_cv_lasso = GridSearchCV(estimator=Lasso(), param_grid={"alpha": np.array([0.1, 1, 10, 100, 1000])}, cv=kf)
gs_cv_lasso.fit(X_train, y_train)
print(gs_cv_lasso.best_params_)
# step 2: zooming-in
gs_cv_lasso = GridSearchCV(estimator=Lasso(), param_grid={"alpha": np.arange(0.03, 0.99, 0.03)}, cv=kf)
gs_cv_lasso.fit(X_train, y_train)
print(gs_cv_lasso.best_params_)
# step 3: zooming-in even further
gs_cv_lasso = GridSearchCV(estimator=Lasso(), param_grid={"alpha": np.arange(0.005, 0.03, 0.005)}, cv=kf)
gs_cv_lasso.fit(X_train, y_train)
print(gs_cv_lasso.best_params_)
# use best regularization strength parameter

