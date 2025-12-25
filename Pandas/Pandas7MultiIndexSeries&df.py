from os import error
import numpy as np
import pandas as pd

# Series is 1D and DataFrames are 2D objects
# But why?
# And what exactly is index?
   

# can we have multiple index in a series?
# index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
# a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
# print(a)
# print(a['cse',2022])
# # agar woh sab koh fethc karna jahan pe cse hai
# print(a['cse']) # == error

# proper way to make a multiindex series
# you have to make a multi index object

# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()

index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
# print(multiindex)
# print(multiindex.levels)

# another way
# pd.MultiIndex.from_product(index_val)

a = pd.MultiIndex.from_product([['cse','ese'],[2019,2020,2021,2022]])
# print(a)
# print(a.levels)


# levels inside multiindex object

# creating a series with multiindex object
s=pd.Series([1,2,3,4,5,6,7,8],index = multiindex)

# how to fetch from such a series
# print(s['cse',2022])
# if all where there is cse
# print(s['cse'])

# this is a 2d dimension series
# we can represnt this through a dataframe to

# unstack
# converts a multiindex series into a df
# saba se andar wale index ko column me convert kar deta
temp =s.unstack()
# print(temp)


# stack()
# this converts a df into a multiindex series

# print(temp.stack())

# so why do we use multiindex series if df 
# can handle the same thing?



# the poit is you can convert higher dimension 
# data into 2d(df) or 1d(series)
# this is the true power of pandas


# MultiIndex DataFrame

branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)

# print(branch_df1)
# print(branch_df1['students'])



# Are columns really different from index?no


# multiindex df from columns perspective
branch_df2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

# print(branch_df2)
# print(branch_df2['delhi'])
# print(branch_df2['mumbai']['avg_package'])
# print(branch_df2.loc[2019])


# Multiindex df in terms of both cols and index

branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)
# # this is a 4d data being represented by a 2d form(data frame)
# print(branch_df3)


# you need multi index objects so you can represnt 
# hihger index object in df or series

 

#  Stacking and Unstacking

# print(branch_df1)
# temp = branch_df1.unstack()
# print(temp)
# print(temp.stack())

# stack = column to row
# unstack = row to column


# Working with multiindex datarframes

# print(branch_df3.head())
# yeh 4d hai
# shape
# print(branch_df3.shape)
# info
# print(branch_df3.info())
# unstack
# print(branch_df3.unstack().info())
# duplicated
# print(branch_df3.duplicated())
# null
# print(branch_df3.isnull)


# extracting rows single from a 4d data frame
# print(branch_df3)

# single rows
# print(branch_df3.loc[('cse',2022)])

# multiple rows

# print(branch_df3.loc[('cse',2019):('ece',2020):2])
# first we defined the starting point then 
# the ending point then the skipping (2)

# using iloc

# print(branch_df3.iloc[0:5:2])


# extracting columns

# print(branch_df3)
# write the name of the column

# print(branch_df3['delhi'])
# agar delhi keh students dekhne
# print(branch_df3['delhi']['students'])

# multiple columns

# delhi ka student and mumbai ka avg package 

# print(branch_df3.iloc[:,1:3])


# extracting both

# cse ka first row and cse ka first row
# delhi ke students and mumbai ke average package

# print(branch_df3.iloc[:5:4,1:3])
# or
# print(branch_df3.iloc[[0,4],[1,2]])



# sort index
# both -> descending -> diff order
# based on one level

# print(branch_df3.sort_index(ascending=False))#descing order
# on both levels

# print(branch_df3.sort_index(ascending=[False,True]))#on one level
# there is false and on one true

# print(branch_df3.sort_index(level=0,ascending=[False]))
# agar only one level ko sort karna hai



# multiindex dataframe(col) -> transpose
# print(branch_df3.transpose())
# rows to column and column to row



# swaplevel

# print(branch_df3.swaplevel())
# this will swap year and branch from branch3

# you can do this on columns too
# print(branch_df3.swaplevel(axis=1))


# Long vs wide Data

# Wide format is where we have a single row
# for every data point with multiple columns 
# to hold the values of various attributes.

# Long format is where, for each data point
#  we have as many rows as the number of 
# attributes and each row contains the value of
#  a particular attribute for a given data point.




# melt = to convert wide to long
# pivot = to convert long to wide

# print(pd.DataFrame({'cse':[120]}))
# print(pd.DataFrame({'cse':[120]}).melt())


# e.g2

# print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}))
# print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}).melt(var_name='branch',value_name='num_students'))


# e.g3

# print(pd.DataFrame({
#     'branch':['cse','ece','mech'],
#     '2020':[100,150,60],
#     '2021':[120,130,80],
#     '2022':[150,140,70]
# }))

# print(pd.DataFrame({
#     'branch':['cse','ece','mech'],
#     '2020':[100,150,60],
#     '2021':[120,130,80],
#     '2022':[150,140,70]
# }).melt())

# is case me har column ko row nahi bana tha
# other wise it will be unreadable
# we have to skip branch

# print(pd.DataFrame({
#     'branch':['cse','ece','mech'],
#     '2020':[100,150,60],
#     '2021':[120,130,80],
#     '2022':[150,140,70]
# }).melt(id_vars=['branch'],var_name='year',value_name='num_students'))
# id_vars mean dont chnage this to row


# death = pd.read_csv('Pandas\\time_series_covid19_deaths_global.csv')
# confirmed = pd.read_csv('Pandas\\time_series_covid19_confirmed_global.csv')
# print(death)
# print(confirmed)


# death1 = death.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_deaths')

# confirm1 = confirmed.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_cases')

# print(confirm1.merge(death1,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_cases','num_deaths']])
# melt is done to convert wide to long
# ususally the database data is in wide format
# so melt is used to make it easir to perform
# analysis on the data