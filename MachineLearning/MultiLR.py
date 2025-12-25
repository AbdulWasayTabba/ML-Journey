# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_regression
# import plotly.express as px
# import plotly.graph_objects as go
# from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# X,y = make_regression(n_samples=100,n_features=2,n_informative=2,n_targets=1,noise=50)

# df = pd.DataFrame({'feature1':X[:,0],'feature2':X[:,1],'target':y})

# print(df.shape)
# print(df.head())
# fig = px.scatter_3d(df, x='feature1', y='feature2', z='target')

# fig.show()

# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=3)

# from sklearn.linear_model import LinearRegression
# lr = LinearRegression()
# lr.fit(X_train,y_train)

# y_pred = lr.predict(X_test)
# print("MAE",mean_absolute_error(y_test,y_pred))
# print("MSE",mean_squared_error(y_test,y_pred))
# print("R2 score",r2_score(y_test,y_pred))

# x = np.linspace(-5, 5, 10)
# y = np.linspace(-5, 5, 10)
# xGrid, yGrid = np.meshgrid(y, x)

# final = np.vstack((xGrid.ravel().reshape(1,100),yGrid.ravel().reshape(1,100))).T
# z_final = lr.predict(final).reshape(10,10)

# z = z_final



# fig = px.scatter_3d(df, x='feature1', y='feature2', z='target')

# fig.add_trace(go.Surface(x = x, y = y, z =z ))

# fig.show()

# print(lr.coef_)

# print(lr.intercept_)




# code 2



from tkinter import NO
import numpy as np


from sklearn.datasets import load_diabetes

X,y = load_diabetes(return_X_y=True)
print(X)
print(X.shape)#there are 10 input columns
# so there will be 11 coeef b0 to b10

print(y)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)

from sklearn.metrics import r2_score

print(r2_score(y_test,y_pred))

print(reg.coef_)
print(reg.intercept_)

# now lets make out own class

class MeraLR:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
    def fit(self,X_train,y_train):
        X_train = np.insert(X_train,0.1,axis=1)
        #calculate coeff
        betas = np.linalg.inv(np.dot(X_train.T,X_train)).dot(X_train.T).dot(y_train)
        #inverse
        self.intercept_ = betas[0]
        self.coef_ = betas[1:]
    
    def predict(self,X_test):
        y_pred = np.dot(X_test,self.coef_)+self.intercept_
        return y_pred

lr = MeraLR()
lr.fit(X_train,y_train)
print(X_train.shape)

print(np.insert(X_train,0.1,axis=1).shape)

y_pred=lr.predict(X_test)

print(r2_score(y_test,y_pred))

print(lr.coef_)

print(lr.intercept_)
