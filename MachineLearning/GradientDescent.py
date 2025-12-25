
# from sklearn.datasets import make_regression
# import numpy as np

# X,y = make_regression(n_samples=4, n_features=1, n_informative=1, n_targets=1,noise=80,random_state=13)

# import matplotlib.pyplot as plt
# plt.scatter(X,y)
# plt.show()

# # lets apply ols to fins slope and intercept value
# from sklearn.linear_model import LinearRegression


# reg = LinearRegression()
# reg.fit(X,y)

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)

# print(reg.coef_)

# print(reg.intercept_)


# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red')



# # Lets apply Gradient Descent assuming slope is constant m = 78.35
# # and let's assume the starting value for intercept b = 0
# y_pred = ((78.35 * X) + 100).reshape(4)
     

# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red',label='OLS')
# plt.plot(X,y_pred,color='#00a65a',label='b = 0')
# plt.legend()
# plt.show()



# m = 78.35
# b = 100

# loss_slope = -2 * np.sum(y - m*X.ravel() - b)
# print(loss_slope)



# # Lets take learning rate = 0.1
# lr = 0.1

# step_size = loss_slope*lr
# print(step_size)


# # Calculating the new intercept
# b = b - step_size
# print(b)
     


# y_pred1 = ((78.35 * X) + b).reshape(4)

# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red',label='OLS')
# plt.plot(X,y_pred1,color='#00a65a',label='b = {}'.format(b))
# plt.plot(X,y_pred,color='#A3E4D7',label='b = 0')
# plt.legend()
# plt.show()



# # Iteration 2
# loss_slope = -2 * np.sum(y - m*X.ravel() - b)
# print(loss_slope)



# step_size = loss_slope*lr
# print(step_size)




# b = b - step_size
# print(b)


# y_pred2 = ((78.35 * X) + b).reshape(4)

# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red',label='OLS')
# plt.plot(X,y_pred2,color='#00a65a',label='b = {}'.format(b))
# plt.plot(X,y_pred1,color='#A3E4D7',label='b = {}'.format(b))
# plt.plot(X,y_pred,color='#A3E4D7',label='b = 0')
# plt.legend()
# plt.show()



# # Iteration 3
# loss_slope = -2 * np.sum(y - m*X.ravel() - b)
# print(loss_slope)
     


# step_size = loss_slope*lr
# print(step_size)



# b = b - step_size
# print(b)



# y_pred3 = ((78.35 * X) + b).reshape(4)

# plt.figure(figsize=(15,15))
# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red',label='OLS')
# plt.plot(X,y_pred3,color='#00a65a',label='b = {}'.format(b))
# plt.plot(X,y_pred2,color='#A3E4D7',label='b = {}'.format(b))
# plt.plot(X,y_pred1,color='#A3E4D7',label='b = {}'.format(b))
# plt.plot(X,y_pred,color='#A3E4D7',label='b = 0')
# plt.legend()
# plt.show()
     



# b = -100
# m = 78.35
# lr = 0.01

# epochs = 100

# for i in range(epochs):
#   loss_slope = -2 * np.sum(y - m*X.ravel() - b)
#   b = b - (lr * loss_slope)

#   y_pred = m * X + b

#   plt.plot(X,y_pred)

# plt.scatter(X,y)








# now we will make a class gd regressor
# fit and predict two features



# from sklearn.datasets import make_regression
# import matplotlib.pyplot as plt
# import numpy as np

# X,y = make_regression(n_samples=100,n_features=1,n_informative=1,n_targets=1,noise=20)
# plt.scatter(X,y)

# # now just do sklearn library lr

# from sklearn.linear_model import LinearRegression

# lr = LinearRegression()

# lr.fit(X,y)

# print(lr.coef_)
# print(lr.intercept_)

# m = lr.coef_

# class GdRegressor:
#     def __init__(self,learning_rate,epochs):
#         self.m = m
#         self.b = -120 #random
#         self.lr = learning_rate
#         self.epochs = epochs

#     def fit(self,X,y):
#         #calculate b using GD
#         for i in range(self.epochs):
#             loss_slope = -2*np.sum(y-self.m*X.ravel()-self.b)
#             self.b = self.b -(self.lr* loss_slope)
#             print(loss_slope,self.b)
#         print(self.b)

# gd = GdRegressor(0.001,50)
# gd.fit(X,y)


# this code was taking m from lr class now we 
# will learn how to do it without knowing m 



from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression




class GDRegressor:
    
    def __init__(self,learning_rate, epochs):
        self.m =100
        self.b = -120
        self.lr = learning_rate
        self.epochs = epochs
    
    def fit(self,X,y):
        for i in range(self.epochs):
          loss_slope_b = -2* np.sum(y - self.m*X.ravel() - self.b)
          loss_slope_m = -2 * np.sum((y - self.m*X.ravel() - self.b ) *X.ravel())
          self.b = self.b - (self.lr*loss_slope_b)
          self.m = self.m - (self.lr * loss_slope_m)
        print(self.m, self.b)
    
    def predict(self,X):
        return self.m * X + self.b



X,y = make_regression(n_samples=100,n_features=1,n_informative=1,n_targets=1,noise=20)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

lr = LinearRegression()
lr.fit(X_train,y_train)
print(lr.coef_)
print(lr.intercept_)

y_pred = lr.predict(X_test)
from sklearn.metrics import r2_score

print(r2_score(y_test,y_pred))

gd = GDRegressor(0.001,50)

gd.fit(X_train,y_train)
y_pred = gd.predict(X_test)


print(r2_score(y_test,y_pred))

