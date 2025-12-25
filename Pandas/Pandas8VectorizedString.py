# from asyncio.windows_events import NULL
# from curses.ascii import NUL, isdigit
# import email
# from operator import le
# from os import name
# from matplotlib import pyplot as plt
# import numpy as np
# import pandas as pd
# import seaborn as sns


# Pivot Table

# The pivot table takes simple
# column-wise data as input,
# and groups the entries into 
# a two-dimensional table that
# provides a multidimensional
# summarization of the data.

# df = sns.load_dataset('tips')#toy dataset
# print(df.head())
# average bill according to gender
# print(df.groupby('sex')[['total_bill']].mean())
# inme se smoker males and non smoker male
# and same with female smokers

# print(df.groupby(['sex','smoker'])[['total_bill']].mean())
# print(df.groupby(['sex','smoker'])[['total_bill']].mean().unstack())

# instead of this we could have used pivot which is shorter

# print(df.pivot_table(index='sex',columns='smoker',values='total_bill'))

# aggregate default is mean

# print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum'))
# print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='count'))


# what is you dont specify the values

# num_cols = df.select_dtypes(include="number").columns
# print(df.pivot_table(index="sex", columns="smoker", values=num_cols))


# multidimnesinoal

# print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],values='total_bill'))

# print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc={'size':'mean','tip':'max','total_bill':'sum'}))

# print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True))
# margin sum kardeta

# plotting graphs
# exp = pd.read_csv('Pandas\\expense_data.csv')
# print(exp)

# month by month har categoryme kitna kharcha hua hai

# exp['Date'] = pd.to_datetime(exp['Date'])
# print(exp.info())
# exp['month']=exp['Date'].dt.month_name()

# exp.pivot_table(index='month',columns='Category',values='INR',aggfunc='sum',fill_value=0).plot()
# plt.show()

# exp.pivot_table(index='month',columns='Income/Expense',values='INR',aggfunc='sum',fill_value=0).plot()
# plt.show()



# What are vectorized operations

# used on textual data

# a = np.array([1,2,3,4])
# print(a*4)

# problem in vectorized opertions in vanilla python

# s = ['cat','mat',None,'rat']
# print([i.startswith('s') for i in s])

# how pandas solve this issue?
# s = pd.Series(['cat','mat',None,'rat'])

# String accessor
# print(s.str.startswith('c'))
# this will work
# and ignore none unlike normal python 
# this is why pandas is better



        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    temp = users.merge(orders,left_on = 'user_id',right_on = 'buyer_id',how = 'inner').reset_index()
    temp = temp[pd.to_datetime(temp['order_date']).dt.year == 2019]
    print(temp)

        

