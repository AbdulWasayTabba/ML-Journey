# Functions

# abstraction
# decomposition 
#  

# how to make 

# def is_even(i):"""info about function """
# logic:x=i%2==0
# return x 

# call fucntion
# is_even(3)


# Let's create a function(with docstring)

# odd ya even

# def is_even(x):
#     """this function returns if a given number
#     is odd or even
#     input: any valid integer
#     output: odd ya even
#     created on : 21 july
#     """
#     if type(x) == int:
#         if x%2 == 0:
#           return 'even'
#         else:
#           return 'odd'
#     else:
#        print('pk')

# to find documentation fo fucntion we do 

# print(is_even.__doc__)

# for i in range(1,11):
#     x = is_even(i)
#     print(x)


# 2 Point of views

# the fucntion should be able to handle all 
# the data types 
# error handling


# when you calling the funtion and the input in it
# is argument 
# but  
# when you are making a fucntion 
# the input is called parameter



# Parameters Vs Arguments

# Types of Arguments

# Default Argument
# Positional Argument
# Keyword Argument

# Default Argument
# you can give default value to parameter
# to handle the fact that the user dosent 
# put anything in the arguments

# def power(a=1,b=1):
#    return a**b

# print(power(5))


# Positional Argument

#  the default sequence is that the
# first argument goes to the first parameter
# the second goes to the second


# Keyword Argument
#over here postion arguments weerent followed
#  keyword argument has precedence over
# postional argument
# you have to remeber the key word not the postion 


# print(power(b=3,a=2))



# *args and **kwargs

# allows us to pass a variable number of 
# non keyword argument

# agar bana hai jo kitne bhi 
# num ko multiply kare
# toh we use args

# def multiply(a,b):
#     return a*b
# multiply(2,3)
# def multiply(a,b,c):
#     return a*b*c
# print(multiply(2,3,3))

# def multiply(*args):
#     product = 1

#     for i in args:
#         product = product*i
#     print(args)    
#     return product
# print(multiply(1,2,3,3,4,4,4,5,5,8))

# args ke andar sare input store ho jate 
# in form of tuple



# **kwargs
# **kwargs allows us to pass any number
#  of keyword arguments.
# Keyword arguments mean that they 
# contain a key-value pair, like a Python dictionary.


# countries and capitals

# def display(**kwargs):

#     for (key,value) in kwargs.items():
#         print(key,'->',value)
# display(india = 'delhi'
#         ,srilanka='columbo',nepal='katwandu'
#         ,pakistan = 'islamabad')
    

# kwargs = dict
# args = tuple 


# points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
# The words “args” and “kwargs” are
#  only a convention,
# you can use any name of your choice



# How Functions are executed in memory?

# when python sees def keyword
# it skips the functions 
# and goes to
# place where the program is called
# (creates a fucntion block)
# then it go back to the def line
# and run the funtion code
# in the end it will return and the fucntion 
# block will be destroyed 

# so a fucntion acts like a independent program
# and has a life span 
# call hone se return tak

# agar return value nahi hai toh 
# the function will return none
# to the place where it is called

# L = [1,2,3]
# print(L.append(4))

# l.append ka function none return karta
# so if we run it we get None


# Variable Scope

# jo variables 
# function ke scope me ate 
# we call them local variable 
# the ones who are in the main program 
# are called global variables

# local can use global 
# global cant use local


# def g(y):
#     print(x)
#     print(x+1)
# x = 5
# g(x)
# print(x)


# def f(y):
#     x = 1#in this x and the global x 
#     x += 1#has no relation they will 
#     print(x)#act as diffrent varibales
# x = 5#in memory
# f(x)
# print(x)


# def h(y):
#     x += 1
# x = 5
# h(x)
# print(x)
# if the function uses 
# the global variable it can use it 
# but cant chnage it hence this fucntion 
# will result in error
# the way it can be done if you use 
# global key word(not recommended)


# def f(x):
#    x = x + 1
#    print('in f(x): x =', x)
#    return x

# x = 3
# z = f(x)
# print('in main program scope: z =', z)
# print('in main program scope: x =', x)


# Nested Functions

# def f():
#     def g():
#         print('inside function g')
#     g()
#     print('inside function f')
# f()
# you cant call g from the main program



# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x =', x)
#     h()
#     return x

# x = 3
# z = g(x)


# def g(x):
#     def h(x):
#         x = x+1
#         print("in h(x): x = ", x)
#     x = x + 1
#     print('in g(x): x = ', x)
#     h(x)
#     return x

# x = 3
# z = g(x)
# print('in main program scope: x = ', x)
# print('in main program scope: z = ', z)




# Functions are 1st class citizens

# e.g all the data types are first class citizens
# because you can return them assign them perform on em
# function are the same thing

# type and id
# def square(num):
#     return num**2
# print(type(square))#fucntion
# print(id(square))
# a = 2
# print(id(a))
# function will act as a data type
# it can do evrything what a list or someother datatype 
# can do

# reassign
# x = square
# print(x(3))
# print(id(x))
#x has same address as square
# you renamed sqaure to x


# deleting a function

# del square
# square(3)#not possuble because deleted


# storing 

# L = [1,2,3,4,square]#will work
# print(L[-1](4))


# fucntion is imutable datatype
# to check we will put in sets

# s = {square}
# print(s)
# hence imutable


# returning a functinm

# def f():
#     def x(a, b):
#         return a+b
#     return x
    
# val = f()(3,4)
# print(val)
#yeh possible hai because bahir wale 
# fucntion ne andar wale ko return kara
# toh woh refernce ho gaya
# otherwise you call
# the nested fucntion from the main program



# function as argument

# def func_a():
#     print('inside func_a')

# def func_b(z):
#     print('inside func_b')
#     return z()

# print(func_b(func_a))


# Benifits of using Funtions

# Code Modularity
# Code Readibility
# Code Reusability


# Lambda Function

# lambda function is a small anonymous function

# A lambda function can take any number of arguments
# ,but can only have one expression

# lambda a,b:a+b

# a = lambda x:x**2
# print(a(4))

# b = lambda x,y:x+y
# print(b(5,2))

# # check if a string has 'a'

# c = lambda f,g:g in f
# print(c('hello','a'))

# odd or even

# d = lambda g:'even' if g%2 == 0 else 'odd'
# print(d(4))


# Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line
# not reusable
# Then why use lambda functions?
# They are used with HOF(higher order functions)


# Higher order function

# a function which returns
# a function
# or 
# a function which recives a function in its input 

# e.g

# def square(x):
#     return x**2
# def cube(x):
#     return x**3

# trnasform is a higher order fucntion
# because in the input it is getting a fucntion
# def transform(f,L):
#     output = []
#     for i in L:
#         output.append(f(i))

#     print(output)
# L = [1,2,3,4,5]

# transform(square,L)
# transform(cube,L)

# instead of creating diffrent functions for 
# square and cube we use lambda

# transform(lambda x:x**2,L)
# transform(lambda x:x**3,L)



# Map (important)

# map expect lamda fucntion
# and iterable


# square the items of a list
# print(list(map(lambda x:x**2,[1,2,3,4,5])))
# print(map.__doc__)

# odd/even labeling of the items

# L = [1,2,3,4,5]
# print(list(map(lambda x:'even' if x%2 == 0 else 'odd',L)))

# fetch names from list of dict

# users = [
#     {
#         'name':'Rahul',
#         'age':45,
#         'gender':'male'
#     },
#     {
#         'name':'Nitish',
#         'age':33,
#         'gender':'male'
#     },
#     {
#         'name':'Ankita',
#         'age':50,
#         'gender':'female'
#     }
# ]
# print(list(map(lambda users:users['name'],users)))




# Fliter (important)

# given list ke andar se kese condition
# ke bases pe filter karta hai

# numbers greater than 5

# l = [3,4,5,6,7]
# l1 = list(filter(lambda x:x>5,l))
# print(l1)
# print(filter.__doc__)


# fetch fruits starting with 'a'

# fruits = ['apple','guava','cherry']
# print(list(filter(lambda x:x.startswith('a'),fruits)))


# Reduce

# import functools 

# sum of all time
# print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))


# find min

# print(functools.reduce(lambda x,y:x if x<y else y,[23,21,233,42,12]))

