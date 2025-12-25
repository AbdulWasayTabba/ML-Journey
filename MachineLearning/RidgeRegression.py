import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes



data = load_diabetes()
# print(data.DESCR)

X = data.data
y = data.target
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=45)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,y_train)

print(lr.coef_)
print(lr.intercept_)

y_pred = lr.predict(X_test)

from sklearn.metrics import r2_score,mean_squared_error

print("r2Core",r2_score(y_test,y_pred))

print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred)))

from sklearn.linear_model import Ridge

r = Ridge(alpha= 0.0001)

r.fit(X_train,y_train)

print(r.coef_)
print(r.intercept_)

y_pred1 = r.predict(X_test)

print("r2Core",r2_score(y_test,y_pred1))

print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred1)))


lr_coefs = lr.coef_
ridge_coefs = r.coef_
features = np.arange(len(lr_coefs))
# If you want feature names:
# features = data.feature_names

plt.figure(figsize=(10,6))
plt.plot(features, lr_coefs, marker='o', label='Linear Regression Coefficients')
plt.plot(features, ridge_coefs, marker='x', label='Ridge Regression Coefficients')
plt.xlabel('Feature Index')
plt.ylabel('Coefficient Value')
plt.title('Linear vs Ridge Regression Coefficients')
plt.legend()
plt.grid(True)
plt.show()