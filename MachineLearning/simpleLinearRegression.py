# Simple Linear Regression 

# (easy to understand)
# implement on more alogrithms 
# like a basic foundation

# this is a supervised ml algorithm

# this solves a regression problem 
# meanign that this is applied on those data
# sets whose output is numerical

# there are three types of linear regression
# 
# 1 simple
# 2 mutli
# 3 polynomial 


# in simple there is one input and one output
# column 

# e.g  cgpa | package

# cgpa  = input 
# package = output 


# multiple if you have more than 1 
# input columns

# cgpa ,gender, 12 aqmrks, state = input 
# package = output


# polynomial lr 

# if data isnt linear means data is a real world data set


# simple lr

# y = mx+b
# m = slope 
# b = y intercept

# you will draw a best fit line
# best fit line = closets to every point 


# from tkinter import NO, Y
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# np.random.seed(42)

# # Generate CGPA values between 5 and 10
# cgpa = np.round(np.random.uniform(5.0, 10.0, 100), 2)

# # Create a realistic correlation: higher CGPA → higher package
# # Suppose package (in LPA) ≈ 0.5 * CGPA + random noise
# noise = np.random.normal(0, 0.5, 100)  # small random variation
# package = np.round(0.5 * cgpa + noise, 2)

# # Make sure packages stay positive
# package = np.clip(package, 1, None)

# df = pd.DataFrame({
#     'cgpa': cgpa,
#     'package': package
# })

# print(df.head)
# # plt.scatter(df['cgpa'],df['package'])
# # plt.xlabel('CGPA')
# # plt.ylabel('Package(in lpa)')
# # plt.show()

# # sab se pehle input and output column alag kardete ho

# X = df.iloc[:,0:1]
# Y = df.iloc[:,-1]

# # next we hide some data 

# # a training set and a test set

# from sklearn.model_selection import train_test_split

# X_train ,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)
# # testsize = 0.2 mean 20% data test me ja raha 

# from sklearn.linear_model import LinearRegression
# lr = LinearRegression()
# lr.fit(X_train,Y_train)
# print("cgpa")
# print(X_test)
# print("package")
# print(Y_test)

# print(lr.predict(X_test.iloc[[1]].values.reshape(1,1)))

# plt.scatter(df['cgpa'],df['package'])
# plt.plot(X_train, lr.predict(X_train))
# plt.xlabel('CGPA')
# plt.ylabel('Package(in lpa)')
# plt.show()

# print("Slope (m):", lr.coef_[0])
# print("Intercept (b):", lr.intercept_)
# y = mx+b


# theory

# package = mx+b
# m(slope) = weighteage(cgpa pe kitna depend karta hai package)
# yeh formula se you find the line which is the formula above
#  there are two solution to fund the line 
# closed form solution and non closed form solution
# closed form solution ko ols bolte hai sklearn uses this 
#non closed form =  technique is called gradient descent
# non closed is used when there are many dimensions and 
# less dimensions closed form is used
# in a class sgdregressor gradient regressor is used
# b = ybar - m xbar
# m = sigma (xi-xbar)(yi-ybar)/sigma(xi-xbar)^2

# error function =n sigma i=1 di^2
# di = (y-yi^)
# y is the actual value and yi is the prediction
# so when we minus that is the error

# so error fucntion = n sigma i=1 (y-y^)^2
# in this we need to find (m,b) jise min error fucntion aye
# yi^ = mxi +b
# ef(m,b) =n sigma i=1 (yi -mxi -b)^2 
# 
# so ab the wuestions is changin m and chanigign b 
# will change ef how ?

# changing one only m or b will result in a parabaola (U) shaoe in graph
# 
# in lr.fit() maxima and minima is done
# de/dm = 0, de/db = 0


# now we will create the class which a sklearn linear regression class
# does

# class MeraLr:
#     def __init__(self):
#         self.m = None
#         self.b = None
    
#     def fit(self,X_train,Y_train):
#         num =0
#         den =0
#         for i in range(X_train.shape[0]):
#            num = num+ ((X_train[i]-X_train.mean())*(Y_train[i]-Y_train.mean()))
#            den = den+((X_train[i]-X_train.mean())*(X_train[i]-X_train.mean()))
#         self.m = num/den
#         self.b = Y_train.mean() - (self.m * X_train.mean())
#         print(self.m)
#         print(self.b)


#     def predict(self,X_test):
#         return self.m*X_test+self.b

# X = df.iloc[:,0].values
# Y = df.iloc[:,1].values

# from sklearn.model_selection import train_test_split
# X_train ,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)
# lr = MeraLr()
# lr.fit(X_train,Y_train)
# print(lr.predict(X_test[1]))
# this will only work for simple lr not multi ones


# Regression Metrics


# 1: MAE (mean absolute error)

# mean point from prediction - actual point
# |y1 - y1^|+|y2-y2^|.....
# then divide by number of points

# mae = n sigma i = 1 |yi-yi^| / n

# you would want mean absoulte error kam se kam
# the whole idea is to reduce the mae
#
# advantage

# mae is always in y 
# so advantage is same unit 
# robust to ourliers

# disadvantage

# we are using modulous so the disadvantage is 
# modulus function graph is not diffreciable at 0


# 2: MSE (mean squared error)

# mse  = n sigma i =1 (yi=y1^)^2 / n
# 
# mse represents the square starting from actualt point 
# to the prediction line and the whole idea is usko kam se kam 
# karna hai

# advantage

# this graph will be diffrentiable at all points
# you can use it as a los function

# disadvantage

# interpret is a bit difficult because
# the answers comes in square like lpa(^2)
# not robust to outliers


# 3:RMSE (root over of MSE)

# RMSE  = root of n sigma i =1 (yi=y1^)^2 / n


# 4: R2 SCORE (coeff of determination, goddness of fit)

# you comapre keh apka linear regression wale line mean line
# se kitna behtar hai

# r2 score = 1 - SSR/SSM

# ssr =  sum of squared error in regression line
# ssm =  sum of sqaured error in mean line

# r2 score = 1- (n sigma i =1  (yi-yi^)^2 /n sigma i =1 (yi-yi^)^2)

# if r2 score is 0 it means than both regression and mean 
# are doing the same error 

# if r2 score is 1 it means that the regression line if perfect 

# this means the more perfect you are moving to r2 score is moving to 1
# and the more you are moving to mean r2 score lean to wards 0

# but what if the r2 score is negative it means that the 
# regression line is doing worse than the mean line


# Adjusted r2 score

# comes when you are putting irreleant data 
# which may increase the r2 score

# adjusted r2 score = 1 -  [1-r2score](n-1) / (n-1-k)]
 
#  n = no of rows
#  k = total number of indepenedent columns

# if relevant columns are added the adjr2score will increase
# if irrelevant data then adjr2score will decrease

# code implementation




# plt.scatter(df['cgpa'],df['package'])
# plt.xlabel('CGPA')
# plt.ylabel('Package(in lpa)')
# plt.show()

# X = df.iloc[:,0:1]
# y = df.iloc[:,-1]





# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)


# from sklearn.linear_model import LinearRegression

# lr = LinearRegression()

# lr.fit(X_train,y_train)

# plt.scatter(df['cgpa'],df['package'])
# plt.plot(X_train,lr.predict(X_train),color='red')
# plt.xlabel('CGPA')
# plt.ylabel('Package(in lpa)')


# from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# y_pred = lr.predict(X_test)

# print(y_test.values)

# print("MAE",mean_absolute_error(y_test,y_pred))


# print("MSE",mean_squared_error(y_test,y_pred))


# print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred)))


# print("MSE",r2_score(y_test,y_pred))
# r2 = r2_score(y_test,y_pred)

# # Adjusted R2 score
# print(X_test.shape)


# adjr2score = 1 - ((1-r2)*(40-1)/(40-1-1))
# print(adjr2score+"adjusted score")

# new_df1 = df.copy()
# new_df1['random_feature'] = np.random.random(200)

# new_df1 = new_df1[['cgpa','random_feature','package']]
# print(new_df1.head())


# plt.scatter(new_df1['random_feature'],new_df1['package'])
# plt.xlabel('random_feature')
# plt.ylabel('Package(in lpa)')
# plt.plot()


# X = new_df1.iloc[:,0:2]
# y = new_df1.iloc[:,-1]


# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)


# lr = LinearRegression()


# lr.fit(X_train,y_train)

# y_pred = lr.predict(X_test)


# print("R2 score",r2_score(y_test,y_pred))
# r2 = r2_score(y_test,y_pred)


# 1 - ((1-r2)*(40-1)/(40-1-2))


# new_df2 = df.copy()

# new_df2['iq'] = new_df2['package'] + (np.random.randint(-12,12,200)/10)

# new_df2 = new_df2[['cgpa','iq','package']]



# print(new_df2.sample(5))


# plt.scatter(new_df2['iq'],new_df2['package'])
# plt.xlabel('iq')
# plt.ylabel('Package(in lpa)')


# np.random.randint(-100,100)


# X = new_df2.iloc[:,0:2]
# y = new_df2.iloc[:,-1]


# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

# lr = LinearRegression()
# lr.fit(X_train,y_train)
# y_pred = lr.predict(X_test)

# print("R2 score",r2_score(y_test,y_pred))
# r2 = r2_score(y_test,y_pred)


# print(1 - ((1-r2)*(40-1)/(40-1-2))  )




# Got it! I’ll rewrite your notes in a **plain text, copy-paste friendly format** so all formulas stay on the same line and nothing breaks when you save it. I’ll also keep it clear and organized.

# ---

# # Linear Regression (Simple & Easy Notes)

# **Concept:**
# Linear Regression finds a best-fit line showing how one variable depends on another.

# **Formula:** y = m*x + b

# * y → predicted value (e.g., package)
# * x → input/feature (e.g., CGPA)
# * m → slope (how much y changes when x increases)
# * b → intercept (value of y when x = 0)

# Example: Predict package from CGPA. m tells how much the package changes per CGPA point.

# ---

# ## Two Methods to Find the Line

# 1. Closed-form solution (OLS – Ordinary Least Squares)

#    * Used for few features. Fast and exact. Used by sklearn.LinearRegression

# 2. Non-closed form (Gradient Descent)

#    * Used for many features or large data. Slower but scalable. Used by SGDRegressor

# ---

# ## Formulas for m and b

# m = Σ((xi - x̄)*(yi - ȳ)) / Σ((xi - x̄)^2)
# b = ȳ - m*x̄

# Where:

# * xi, yi = each data point
# * x̄, ȳ = mean of all x’s and y’s

# Example: X = [1,2,3], Y = [2,3,5] → plug in to calculate m and b

# ---

# ## Error Function (Cost Function)

# Error for one point: di = yi - ŷi
# Total Error (Sum of Squared Errors): E(m,b) = Σ(yi - (m*xi + b))^2
# Goal: find m and b that **minimize this error**

# Changing m or b creates a **U-shaped curve**, bottom = minimum error. This is what `.fit()` does internally.

# ---

# ## Example: Custom Linear Regression Class

# ```
# class MeraLr:
#     def __init__(self):
#         self.m = None
#         self.b = None

#     def fit(self, X_train, Y_train):
#         num = 0
#         den = 0
#         for i in range(X_train.shape[0]):
#             num += (X_train[i] - X_train.mean()) * (Y_train[i] - Y_train.mean())
#             den += (X_train[i] - X_train.mean())**2
#         self.m = num / den
#         self.b = Y_train.mean() - self.m * X_train.mean()

#     def predict(self, X_test):
#         return self.m * X_test + self.b
# ```

# Works only for simple linear regression (one feature).

# ---

# # Regression Evaluation Metrics

# **1. MAE (Mean Absolute Error)**
# MAE = Σ|yi - ŷi| / n

# * Average distance between predicted and actual values
# * Unit = same as y
# * Robust to outliers
# * Not differentiable at 0 (modulus problem)

# **2. MSE (Mean Squared Error)**
# MSE = Σ(yi - ŷi)^2 / n

# * Squares errors before averaging
# * Differentiable, good for training models
# * Unit = y^2
# * Sensitive to outliers

# **3. RMSE (Root Mean Squared Error)**
# RMSE = √(Σ(yi - ŷi)^2 / n)

# * Square root of MSE, back to original units

# **4. R² Score (Coefficient of Determination)**
# R² = 1 - SSR/SSM

# * SSR = Σ(yi - ŷi)^2 → error with regression line
# * SSM = Σ(yi - ȳ)^2 → error with mean line
# * Interpretation:

#   * 1 → perfect fit
#   * 0 → same as mean line
#   * <0 → regression worse than mean

# **5. Adjusted R² Score**
# Adjusted R² = 1 - ((1 - R²)*(n - 1)/(n - k - 1))

# * n = number of samples
# * k = number of independent features
# * Penalizes irrelevant features

# ---

# ## Summary Table

# | Metric | Formula                      | Best When            | Unit      | Notes                         |           |                    |
# | ------ | ---------------------------- | -------------------- | --------- | ----------------------------- | --------- | ------------------ |
# | MAE    | Σ                            | yi - ŷi              | / n       | Easy interpretation           | Same as y | Robust to outliers |
# | MSE    | Σ(yi - ŷi)^2 / n             | Training models      | y^2       | Differentiable                |           |                    |
# | RMSE   | √(Σ(yi - ŷi)^2 / n)          | Model comparison     | Same as y | Penalizes large errors        |           |                    |
# | R²     | 1 - SSR/SSM                  | Check model fit      | None      | 0-1, can be <0                |           |                    |
# | Adj R² | 1 - ((1 - R²)*(n-1)/(n-k-1)) | Multi-feature models | None      | Penalizes irrelevant features |           |                    |

# ---

# If you want, I can also **add a super short numeric example** showing **how to calculate m, b, MAE, MSE, and R² by hand with 3-4 points**. This makes it super easy to remember.

# Do you want me to do that?

