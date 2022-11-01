from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ================ PREPARE THE DATA ================
# load the data
X, y = datasets.load_iris(return_X_y=True, as_frame=False)
# split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=int(0.25*X.shape[0]), stratify=y)
# fit the standard scaler to the train data
scaler_ = StandardScaler()
X_train = scaler_.fit_transform(X_train)
# apply the standard scaler to test data
X_test = scaler_.transform(X_test)


# ================ FIT THE DECISION TREE CLASSIFIER ================
# fit the decision tree on the data
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
dtree.score(X_test, y_test)
