# Data Frame

# jab bhi koi tabular data hota hai 
# pandas usse dataframe bula ta hai
# basically 2d structure of data consiting 
# of rows and columns

# data frame me a single
#  column and a single row is called
# series


# creating Dataframe

import numpy as np
import pandas as pd

# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

student = pd.DataFrame(student_data,columns=['iq','marks','package'])

# using a dictionary

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}
students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
# print(students)


# read_csv

movie = pd.read_csv('C:\\Users\HP\\Desktop\\datascienceNumpy\\Pandas\\movies.csv')
# print(movie)


ipl = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\ipl-matches.csv')
# print(ipl)


# DataFrame Attributes and Methods

# shape
# print(movie.shape)
# print(ipl.shape)

# dtypes
# print(movie.dtypes)
# print(ipl.dtypes)

# index
# print(movie.index)
# print(ipl.index)

# columns
# print(movie.columns)
# print(ipl.columns)

# # values
# print(student.values)
# print(ipl.values)


# head and tail same as series
# top data and bottom data

# print(movie.head(2))
# print(ipl.tail(3))

# sample 
# randomly aik row nikala hai
# print(ipl.sample(5))

# info
# print(movie.info())

# tells non_null count of every column
# data type of evry column
# column name and index,
# memory usage

# print(ipl.info())

# describe

# print(movie.describe())
# this will automatically detect which columns are
# numerical and operate on em
# print(ipl.describe())

# isnull
# keh apke data me null values hai ya nahi
# print(movie.isnull().sum())

# duplicated
# koi duplicated row hai?
# print(movie.duplicated().sum())
# sum ke wajah se total number of duplicated rows a jaye ge
# print(students.duplicated().sum())

# rename
# yeh column ke name ko rename kar deta hai
# print(students)
# students.rename(columns={'marks':'percent','package':'LPA'},inplace=True)
# yeh permanent chnage nahi hota but to make it
# we do inplace = true
# to chage the name fo the column first inside the rename
# function we make a dictionary and in that
# we write th eold name then the new name
# print(students)


# Math Methods

# sum->axis argument

# print(movie.sum)
# yeh har column ke ooper sum apply kar dega
# even if string hai

# but if you want you can apply on rows
# print(students.sum(axis=1))
# yeh row wise sum kar raha

# this is accesible to alll the math functions

# print(students.mean(axis=1))

# print(students.median(axis=1))

# print(students.min())

# print(students.max())

# print(students.std())

# print(students.var())


# Selecting cols from a Dataframe

# single col

# print(movie['title_x'])
# writing the exact name of the column

# this is a series
# print(type(movie['title_x']))

# print(ipl['Venue'])


# multiple columns

# fancy indexing
# print(movie[['title_x','actors','year_of_release']])

# this is a dataframe type

# so if you take out a single column from 
# a dataframe it will be a series
# otherwise more than one = dataframe

# print(type(movie[['title_x','actors','year_of_release']]))

# print(ipl[['Team2','Team1','WinningTeam']])

# the order of the labeling matter
# e.g in this sceario team 2 column will come
# first then team1 will come then
# WinningTeam


# Selecting Rows

# iloc = Searches using index Positions
# loc = Searches using index labels

# iloc

# print(movie.iloc[0])
# this is a series because it is a 
# single row
# print(type(movie.iloc[0]))

# multiple rows

# print(movie.iloc[0:5])
# print(movie.iloc[0:16:2])

# fancy indexing

# print(movie.iloc[[0,4,5]])


# loc
# print(students)
# print(students.loc['nitish'])
# print(students.loc['nitish':'rishabh':2])

# loc wale me last is isncluded 
# but not in iloc

# fancy indexing

# print(students.loc[['nitish','ankit']])

# yeh same cheez iloc ho sakhte

# print(students.iloc[0:5])


# Selecting both rows and cols

# if i want to fetch first three movie but i 
# only want the first three columns To 

# print(movie.iloc[0:3,0:3])
# or
# print(movie.loc[0:2,'title_x':'poster_path'])

# diff hai iloc
# me index postion batate ho
# but in loc 
# you will provide the name


# Filtering a DataFrame

# print(ipl.head(2))

# find all the final winners

# mask = ipl['MatchNumber'] == 'Final'
# new_df = ipl[mask]
# print(new_df[['Season','WinningTeam']])

# # or

# print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])


# how many super over finishes have occured

# print(ipl[ipl['SuperOver'] == 'Y'].shape[0])

# shape tell rows and columns of a data frame

# how many matches has csk won in kolkata

# print(ipl[(ipl['City'] == 'Kolkata')&(ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

# toss winner is match winner in percentage

# print(ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0]*100)

# movies with rating higher than 8 and votes>10000

# print(movie[(movie['imdb_rating'] > 8)&(movie['imdb_votes'] >10000)])

# Action movies with rating higher than 7.5

# mask1 = movie['genres'].str.split('|').apply(lambda x:'Action' in x)
# mask1 = movie['genres'].str.contains('Action')
# mask2 = movie['imdb_rating']>7.5
# print(movie[mask1 & mask2])



# Adding new Cols
# 
# completely new
# movie['Country'] = 'India'
# print(movie.head())


# From existing col
# movie.dropna(inplace=True)#to remove null values
# movie['lead actor']= movie['actors'].str.split('|').apply(lambda x:x[0])
# print(movie.head())


# Important Dataframe Functions

# astype
# print(ipl.info())
# ipl['ID'] = ipl['ID'].astype('int32')
# print(ipl.info())

# ipl['Season'] = ipl['Season'].astype('category')
# ipl['Team1'] = ipl['Team1'].astype('category')
# ipl['Team2'] = ipl['Team2'].astype('category')
# print(ipl.info())








