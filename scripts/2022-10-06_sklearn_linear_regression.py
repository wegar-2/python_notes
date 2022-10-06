import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


# set random seed
np.random.seed(1234)
# set number of samples
N = 1000

# generate artificial data for linear regression: y = 5*X1 + 10*X2 -3*X3 + error_term
# error_term ====> et;
# et ~ N(0, 20)
sigma_et = 20
et = np.random.normal(loc=0, size=N, scale=sigma_et).reshape(-1, 1)
X1 = np.random.uniform(low=0, high=10, size=N).reshape(-1, 1)
X2 = np.random.uniform(low=10, high=8, size=N).reshape(-1, 1)
X3 = np.random.uniform(low=15, high=100, size=N).reshape(-1, 1)
y = 5*X1 + 10*X2 - 3*X3 + et
X = np.concatenate([X1, X2, X3], axis=1)

# save the data on the linear regression
df = pd.DataFrame(data=np.concatenate([X, y], axis=1), columns=["X1", "X2", "X3", "y"])
df.to_csv(
    os.path.join(os.getcwd(), "..", "data", "linear_regression_artificial_data.csv")
)

# fit the linear regression model
linreg = LinearRegression()
linreg.fit(X=X, y=y)
y_hat = linreg.predict(X=X)

# calculate R-Squared
print(r2_score(y_true=y, y_pred=y_hat))

# do a plot
plt.scatter(x=y, y=y_hat)
plt.show()
