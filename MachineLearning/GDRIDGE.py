import re
from sys import api_version
from sklearn.datasets import load_diabetes
from sklearn.metrics import r2_score
import numpy as np



X,y = load_diabetes(return_X_y=True)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)

from sklearn.linear_model import SGDRegressor
reg = SGDRegressor(penalty='l2',max_iter=500,eta0=0.1,learning_rate='constant',alpha=0.001)

reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)

print("r2Score",r2_score(y_test,y_pred))
print(reg.coef_)
print(reg.intercept_)


# you can also put gd using ridge

from sklearn.linear_model import Ridge

reg1 = Ridge(alpha=0.001,max_iter=500,solver="sparse_cg")#yeh solver se gd

reg1.fit(X_train,y_train)
y_pred1 = reg1.predict(X_test)
print("r2Score",r2_score(y_test,y_pred1))
print(reg1.coef_)
print(reg1.intercept_)


class MeraRidgeGD:
    
    def __init__(self,epochs,learning_rate,alpha):
        
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.alpha = alpha
        self.coef_ = None
        self.intercept_ = None
        
    def fit(self,X_train,y_train):
        
        self.coef_ = np.ones(X_train.shape[1])
        self.intercept_ = 0
        thetha = np.insert(self.coef_,0,self.intercept_)
        
        X_train = np.insert(X_train,0,1,axis=1)
        
        for i in range(self.epochs):
            thetha_der = np.dot(X_train.T, X_train).dot(thetha) - np.dot(X_train.T, y_train) + (self.alpha * np.insert(thetha[1:], 0, 0))
            thetha = thetha - self.learning_rate*thetha_der
        
        self.coef_ = thetha[1:]
        self.intercept_ = thetha[0]
    
    def predict(self,X_test):
        
        return np.dot(X_test,self.coef_) + self.intercept_
    
    
reg = MeraRidgeGD(epochs=500,alpha=0.001,learning_rate=0.005)


reg.fit(X_train,y_train)

y_pred = reg.predict(X_test)
print("R2 score",r2_score(y_test,y_pred))
print(reg.coef_)
print(reg.intercept_)