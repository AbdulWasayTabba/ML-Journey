import numpy as np
# diffrence in python list and numpy
# speed 
# memory
# convinience

# speed 

# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c = []
# import time
# start = time.time()
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(time.time()-start)




# a = np.arange(10000000)
# b = np.arange(10000000,20000000)
# import time
# start = time.time()
# c=a+b
# print(time.time()-start)

# now advantage in terms of memory

# a = [i for i in range(10000000)]
# import sys 
# print(sys.getsizeof(a))

# # # numpy

# a1 = np.arange(10000000,dtype=np.int32)
# print(sys.getsizeof(a1))

# the memory taken by both the python list and 
# numpy was the same at first but using astype 
# and changing the data type made the numpy take 
# half the memory compared to python list



# Advanced Indexing

# Normal indexing and slicing

# a = np.arange(24).reshape(6,4)
# print(a)
# print()
# print(a[1,2])

# fancy indexing
# fancy indexing me square bracket me list pass 
# kar dete aur list me 
# jo bhi chiye hota hai uska
# index postion de dete ho 

# print(a[[0,2,3]])

# print(a[[0,2,3,5]])

# print(a[:,[0,2,3]])

# boolean indexing 
# condition ke basis pe item nikalne 
# ke liye
# e.g only those numbers who are divisible from 5

# a = np.random.randint(1,100,24).reshape(6,4)
# print(a) 

# q1) find all the numbers greater than 50
# print(a>50) # this is relational
# now what you can do is put the answer of the boolean
# in the orginal array this is called boolean mask
# jahan jahan true ho ga wohi items bache ge

# print(a[a>50])

# method to filter data based on a condition

# q2) find out even numbers
# print(a%2==0)
# print(a[a%2==0])


# q3)nums which are greater than 50 and even

# print((a>50) & (a%2==0))
# print(a[(a>50) & (a%2==0)])
# hamne ne '&' use kara cause this is bitwise one
#  we are doing boolean indexing

# 'and' is a logical and 

# q4) not didvisuble by 7(
# print(a[a%7!=0])
# print(a[~(a%7==0)])#both are nots


#Broadcasting
# describbes how numpy treats diffrent shapes
# array during arthemetic operations
#the smaller array is broadcast across the larger 
# array so they have compatible shapes


#same shape

# a = np.arange(6).reshape(2,3)
# b = np.arange(6,12).reshape(2,3)

# print(a)
# print(b)
# print()
# print(a+b)

#diff shape

# a = np.arange(6).reshape(2,3)
# b = np.arange(3).reshape(1,3)#diff size
# print(a)
# print()
# print(b)
# print()
# print(a+b)

# yeh diff shapes bhi add ho sakhte hai
# this is possible because of broadcasting



# . Make the two arrays have the same number of dimensions.

# If the numbers of dimensions of the two arrays are different
# , add new dimensions with size 1 to the head of the array 
# with the smaller dimension.
# 2. Make each dimension of the two arrays the same size.

# If the sizes of each dimension of 
# the two arrays do not match, dimensions with 
# size 1 are stretched to the size of the other array.
# If there is a dimension whose size is not 1 
# in either of the two arrays, it cannot be broadcasted,
#  and an error is raised.


# a = np.arange(12).reshape(4,3)
# b = np.arange(3)
# print(a)
# print(b)
# print(a+b)

# a = np.arange(12).reshape(3,4)
# b = np.arange(1)
# print(a)
# print(b)
# print(a+b)
# over here broadcasting wont work
# because there dimensions cant be matched



# a = np.arange(3).reshape(1,3)
# b = np.arange(3).reshape(3,1)
# print(a)
# print(b)
# print(a+b)

# step to solve 2 and 4,2
# first you make the a1 into 2d
# 1,2 and 4,2
# then you strech 1 to 4
# 4,2  and 4,2 hence solvable if they 
# arent same not solvable
# and you can only strech 1 not any other num

# broadcasting is used in a technique called
# vectorization


# working with mathematical formulas

# a = np.arange(10)
# print(np.sin(a))


# sigmoid ##important##

# s(x) = 1/1+e^-x

# we are making a function using numpy

# def sigmoid(array):
#     return 1/(1+np.exp(-(array)))
# import time
# start = time.time()
# a = np.arange(100)
# print(sigmoid(a))
# print(start-time.time())



# mean squared error
# MSE =(actual - predicted)**2

# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)
# print(actual)
# print(predicted)

# def mse(actual,predicted):
#   return  np.mean((actual-predicted)**2)
  
# print(mse(actual,predicted))


# how to deal with missing values /
# working with missing values
# e.g in form 

# a = np.array([1,2,3,4,np.nan,6])
# nan and null is similar but not really
# np.nan se missing values create karte

# print(a)

# print(np.isnan(a))#this function asks if you are a 
# missing value or not 
# ab missing mil gaye but i wanted existing so 
# i will aply not(~)

# print(~(np.isnan(a)))




# Plotting Graphs

# plotting a 2d plot
# x=y 

import matplotlib.pyplot as plt
# x = np.linspace(-10,10,100)

# print(x)
# y = x
# print(y)

# # # ab matplotlib use kare ge
# print()
# plt.plot(x,y)
# plt.xlabel('X values')  # Adding labels for clarity
# plt.ylabel('Y values')
# plt.title('Graph of y = x')
# plt.grid(True)  # Adds grid lines
# plt.show()

# y=x^2  parabola

# x = np.linspace(-10,10,100)
# y = x**2
# plt.plot(x,y)
# plt.grid(True)
# plt.show()

# y = sin(x)

# x = np.linspace(-10,10,100)
# y = np.sin(x)
# plt.plot(x,y)
# plt.grid(True)
# plt.show()


# y = x*log(x)

# x = np.linspace(-10,10,100)
# y =x *np.log(x)
# plt.plot(x,y)
# plt.show()

# sigmoid ka graph
# x = np.linspace(-10,10,100)
# y= 1/(1+np.exp(-(x)))
# plt.plot(x,y)
# plt.show()








