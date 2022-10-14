import pandas as pd
import sklearn.metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


# set process parameters
fl_train_set_pctg = 0.8
int_folds = 5

# load the dataset
df_X, df_y = datasets.load_iris(return_X_y=True, as_frame=True)
print(df_X.describe())
print(df_y.unique())
df_y = pd.DataFrame(df_y)
print(df_y.head())
print(df_y.groupby(["target"])["target"].count())
X, y = datasets.load_iris(return_X_y=True, as_frame=False)

# split into test and train samples
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=int(X.shape[0]*fl_train_set_pctg), random_state=1234)

# create KFolder
kfolder = KFold(n_splits=int_folds)

# fit a SINGLE KNeighbors model and do prediction
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
y_test_hat = model.predict(X_test)


# fit multiple KNeigbors models using cross_val_score
res_cross_val_score = cross_val_score(model, X, y, cv=kfolder)
print(res_cross_val_score)

# fit multiple KNeigbors models using cross_validate
res_cross_validate = cross_validate(model, X, y, cv=kfolder)
for iter_key, iter_val in res_cross_validate.items():
    print("key: ", iter_key)
    print("value: ", iter_val)

# doing the cross validation across multiple numbers of neighbors
params_grid = {
    "n_neighbors": [3, 4, 5, 7, 10]
}

grid_search_res = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid=params_grid,
    cv=KFold(n_splits=5)
)
grid_search_res.fit(X_train, y_train)
y_test_hat_gs = grid_search_res.predict(X_test)

