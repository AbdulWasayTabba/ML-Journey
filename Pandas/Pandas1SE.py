# What is Pandas
# Pandas is a fast, powerful, flexible
#  and easy to use open source data
#  analysis and manipulation tool, 
# built on top of the Python programming language.

# https://pandas.pydata.org/about/index.html

# Pnadas me objects hote hai 
# jese python me tuple aur lists etc

# pandas me series datafranme

# Pandas Series
# A Pandas Series is like a 
# column in a table. It is a 1-D array
#  holding data of any type.

# basiabllyy 1d set of numbers ko ap 
# series bula sakhte ho

# importing pandas

import pandas as pd
import numpy as np

# series from Lists

# string

# country = ['India','Pakistan','USA','Nepal','Srilanka']
# print(pd.Series(country))

# nutshell me 
# series me do cheeze hote hai
# idex aur uka value
# e.g 0 India
# 1 Pakistan

# and series string ko object data type assign karta hai

# integers

runs = [13,24,56,78,100]
runs_ser = pd.Series(runs).astype('Int32')

# isme dtype int64 default
# mene astype use karke chnage kara

# custom index

# marks =[67,57,89,100]
# subjects = ['math','english','science','hindi']
# ab i want keh marks value bane aur 
# subjects index
# print(pd.Series(marks, index = subjects))
# woh aise ho ga object/value ke bad , then index = subjects

# series object ko name bhi de sakhte ho 
# to call it in the future

# marks = pd.Series(marks, index = subjects,name = 'my marks')
# print(marks)


# Series in Dictionary

# marks = {
#     'math':67,
#     'english':57,
#     'science':89,
#     'hindi':100
# }

# marks1 = pd.Series(marks,name = 'mere marks')
# print(marks1)
# marks1 is a object of series class now 
# jese oop me hota tha
# dictionary me automatically keys index 
# aur value = value

# print(marks1.size)
# this tells kitne items hai 

# print(marks1.dtype)
# data type

# print(marks1.name)
# series object ka name

# print(marks1.is_unique)
# series me sare items unique hai ya nahi
# of true matlab unique warna false

# pd.Series([1,2,3,4,5,1]).is_unique
# this will return false

# print(marks1.index)
# isme sare ke sare index values stored ho ge
# jese marks me subject names
# because in dictinary key are index

# print(marks1.values)
# print(type(marks.values))
# yeh sare ke sare marks nikalde ga 
# inside a numpy array


# Series using read_csv

# iska kaam hota hai csv file ko read karna
# csv file is liek a excel file 
# ,separated

# print(type(pd.read_csv('C:\\Users\\HP\Desktop\\datascienceNumpy\\Pandas\\subs.csv')))
# yeh data frame type hai


# read.csv defaulty pe data frame me karta
# to make it a series
# we will do this
# using squeeze
subs = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\subs.csv').squeeze("columns")
# print(subs)

# isme ooper ke 5 dekh rahe and last keh
# middle ke sare truncate ho rahe hai
# pandas does this for convienice because 
# if 100000000 rows ho jao toh
# scroll bohot karna parhe ga


# now the data which i am importing has 2 columns

vk = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
# print(vk)



# ab bollywood wale file ko import

b = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\bollywood.csv',index_col='movie').squeeze("columns")
# print(b)


# Series Method

# head an tail method

# head gives data ka preview

# print(subs.head())
# this will give first 5 rows

# print(vk.head(3))
# this will give 
# first 3

# tail will give last rows

# print(vk.tail())
# last 5 mathces ke runs

# print(vk.tail(10))

# last 10 matches ke runs


# sample

# yeh randomly poore data me se
# koi aik movie ke row dekhaye ga

# print(b.sample())

# isme bhi specify kar skahte ho number

# print(b.sample(5))

# sample tab use hota when there is a bias 
# like the there is class and in the stats
# the top students will be on top of the tabel adn the 
# weak students will be on the bottoam 
# so you will use sample then


# value_counts
# 
# every item ke freuqency bata

# in movie if har actor ne kitne movie ke hai

# print(b.value_counts())


# sort_values -> inplace

# q = virat kholi ka ipl me highest score kitna hai

# print(vk.sort_values())
# sorted in ascending order

# print(vk.sort_values(ascending=False))
# descending order

# using this you can get max

# print(vk.sort_values(ascending=False).head(1).values[0])
# to get the maximum runs

# yeh sort permanent chnages nahi karta hai
# temperory chnages karta
# but if you want you can do permanent chnages

# print(vk.sort_values(inplace=True,ascending=False))
# permanent changes



# sort index -> inplace

# same thing as sortvalues but with index

# if movies name ko alphabetcally sort karna hai

# print(b.sort_index())

# isme bhi inplace ka option hai
# to make the change permanent


# Series Maths Methods

# count
# saare items ko counts karta hai 
# but it is diffrent from size
# beacuse it dosent count the missing values

# print(vk.count())

# sum ,product

# print(subs.sum())
# 
# print(subs.prod())


# Statiscal methods

# mean->> median->mode->std->var 

# print(subs.mean())

# print(vk.median())

# print(b.mode().values[0])

# print(subs.std())

# print(vk.var())


# min->max

# print(subs.max())
# print(subs.min())


# describe

# provides a summary

# print(vk.describe())
# print(subs.describe())



# Series Indexing

# integer indexing

# x = pd.Series([12,13,14,35,46,57,58,79,9])
# print(x[0])

# negative indexing
# print(x[-1])
# this wont work
# because series positive indexing pe kam karta
# negative pe nahi
# if index is string toh hi kam kare ga 
# thora weird hai


# print(b['Uri: The Surgical Strike'])
# print(b.iloc[0])


# Slicing

# aik sath multiple items fetch karna

# vk ne 5 se leke 15 matches me ktine runs banaye

# print(vk[5:16])

# negative slicing

# last 5 matches
# print(vk[-5:])

# print(b[-5:])

# har alternate movie

# print(b[::2])


# fancy indexing

# vk ne 1 3 5 6 match me kya runs banaye

# print(vk[[1,3,5,6]])

# from label

# print(b['Awara Paagal Deewana'])


# till now we were only reading
# but we can also edit it /write

# Editing Series


# using index

# marks1[1] = 100
# print(marks1)

# what if index does not exist

# marks1['sst'] = 90
# print(marks1)
# agar woh index wale nahi woh 
# create kar de ga
# jese marks1 me sst nahi tha
# tohy usne mark1 me add kar diya


# slicing

# runs_ser[2:4] = [100,90]
# print(runs_ser)


# fancy indexing

# runs_ser[[0,3,4]] = [0,0,0]
# print(runs_ser)


# label
# b['Company (film)'] = 'Alia Bhatt'
# print(b)

# but usually read operation ap perform karte ho 
# in real world data but pandas has 
# given us a option to edit 


# Series with Python Functionalities


# len.type/dir/sorted/min/max

# print(len(subs))
# print(type(subs))
# print(dir(subs))#all atrubutes and methods
# print(sorted(subs))#output in list
# print(min(subs))
# print(max(subs))


# type conversion
# print(list(marks1))
# print(dict(marks1))

# membership operator

# print('Saathiya (film)' in b)#true
# by default in operator works on 
# index not value
# e.g
# print('Alia Bhatt'in b)#false
# to make it work we do this
# print('Alia Bhatt' in b.values)#true



# loop work on values default pe

# for i in b:
#     print(i)
    # all actors
# to make it work on index we do 
# for i in b.index:
#     print(i)
    # #all movies

# Arithmetic Operators(broadcasting)
# print(marks1)
# question har subject me 100 marks ane se kitne reh gaye
# print(100 - marks1)

# Relational Operators
# # which match did he make more than 50
# print(vk >= 50)


# Boolean indexing on Series

# Find no of 50's and 100's scored by kohli
# print(vk[vk>=50].size)

# find number of ducks

# print(vk[vk == 0].size)

# Count number of day when I had more than 200 subs a day

# print(subs[subs>200].size)

# find actors who have done more than 20 movies
# num_movies = b.value_counts()
# print(num_movies[num_movies>20])


# Plotting Graphs on Series Object

import matplotlib.pyplot as plt
# print(subs.plot())
# plt.show()

# num = b.value_counts().head(20)
# num.plot(kind='pie')
# plt.show()



# Q1)
# Series Creation (Lists)
# Create a pd.Series of your 
# top 5 favorite foods with 
# custom indexes as numbers (101, 102, …).
# Print the dtype and check if it’s unique or not.
# import pandas as pd
# fav_food = ['dal','pizza','keyma','burger','steak']
# numbers = [i+1 for i in range(100,105) ]
# print(pd.Series(fav_food,index=numbers))

# Q2)
# Series Creation (Dictionary)
# Make a dictionary of 4 countries 
# as keys and their populations (in millions)
# as values. Convert it into a 
# Pandas Series named "Population".
#  Print its index, values, and name.

# import pandas as pd
# pop = {
#     'Paksitan':100000,
#     'India':300000,
#     'America':500000,
#     'Japan':50000
# }
# print(pd.Series(pop,name='Population'))


# CSV Import and Squeeze
# Import the subs.csv file, 
# convert it into a Series
# using .squeeze("columns"), and print:
# First 5 rows (head)
# Last 5 rows (tail)
# 5 random samples (sample)

# import pandas as pd
# subs = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\subs.csv').squeeze('columns')
# print(subs)
# print(subs.head(5))
# print(subs.tail(5))
# print(subs.sample(5))


# Q4)
# Value Counts
# From your bollywood.csv file, 
# use value_counts() to
# find the top 10 actors with the most movies.

# import pandas as pd
# movie = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\bollywood.csv',index_col='movie').squeeze('columns')
# num = movie.value_counts(ascending= False)
# print(num.head(10))


# Q5)
# Sorting Values
# From the vk Series (Kohli IPL runs),
# sort it in descending order
# and find his highest 3 scores.

# import pandas as pd
# runs_ser = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\kohli_ipl.csv',index_col='match_no').squeeze('columns')

# print(runs_ser.sort_values(ascending= False).head(3).values)


# Q6)
# tatistical Functions
# From the subs Series:
# Find the mean, median, std (standard deviation), and var.
# Find the min and max.
# Use .describe() to summarize.

# import pandas as pd
# subs = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\subs.csv').squeeze('columns')
# print(subs.mean())
# print(subs.median())
# print(subs.std())
# print(subs.var())
# print(subs.min())
# print(subs.max())
# print(subs.describe())

# Q7)
# Indexing & Slicing
# From the vk Series:
# Print runs scored in matches 5 to 15 (slice).
# Print runs in matches [1, 5, 7, 10] (fancy indexing).
# Print the last 10 matches using negative slicing.

# import pandas as pd
# runs_ser = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\kohli_ipl.csv',index_col='match_no').squeeze('columns')
# print(runs_ser[4:15])
# print(runs_ser[[1,5,7,10]])
# print(runs_ser[-10:])


# Q8)
# Editing Series
# In the marks1 Series,
#  update 'english' marks to 80.
# Add a new subject 
# 'computer' with marks 95.
# Update the first two
#  values in runs_ser to [0, 0].

# import pandas as pd
# result = {
#     'math':67,
#     'english':57,
#     'science':89,
#     'hindi':100
# }
# resultmarks = pd.Series(result,name = 'mere marks')
# resultmarks['english'] = 80
# resultmarks['computer'] = 95
# print(resultmarks)
# runs_ser = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\kohli_ipl.csv',index_col='match_no').squeeze('columns')
# runs_ser[:2] = [0,0]
# print(runs_ser.head())

# Q9)
# Boolean Indexing
# From vk, count how
#  many fifties (runs ≥ 50).
# Count how many ducks
#  (runs = 0).
# From subs, count how
#  many days had more than 200 subs

# import pandas as pd

# runs_ser = pd.read_csv('C:\\Users\\HP\\Desktop\datascienceNumpy\\Pandas\\kohli_ipl.csv',index_col='match_no').squeeze('columns')
# subs = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\subs.csv').squeeze('columns')
# print(runs_ser[runs_ser.values>50].size)
# print(runs_ser[runs_ser.values == 0].size)
# print(subs[subs.values>200].size)


# Q10)
# Plotting
# Plot the top 20 
# actors (from b.value_counts().head(20)) as a bar chart.
# Plot the subs Series as a line chart.

# import pandas as pd
# import matplotlib.pyplot as plt

# movie = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\bollywood.csv',index_col='movie').squeeze('columns')
# num = movie.value_counts(ascending= False).head(20)
# num.plot(kind='bar')
# plt.show()