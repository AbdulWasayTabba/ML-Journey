from cProfile import label
from enum import auto
from operator import index
from turtle import color, width
from matplotlib import axis, markers
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

# Q1)
# runs = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\sharma-kohli.csv')
# print(runs)
# plt.plot(runs['index'],runs['RG Sharma'],color = 'black',linestyle = 'dashed',marker = 'D',label = 'RG Sharma')
# plt.plot(runs['index'],runs['V Kohli'],color = 'blue',linestyle='dashed',marker = 'D',label = 'V Kholi')
# plt.legend(loc = 'lower right')
# plt.xlim(2014,2019)
# plt.ylim(200,900)
# plt.show()

# Q2)
# prices= [48000,54000,57000,49000,47000,45000,450000]
# years= [2015,2016,2017,2018,2019,2020,2021]
# plt.plot(years,prices)
# plt.show()

# plt.plot(years,prices)
# plt.ylim(40000,70000)
# plt.show()


# Q3)
# sr = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\batter.csv')


# plt.scatter(sr['avg'],sr['strike_rate'],color = 'red',s = sr['runs']/sr['avg'])
# plt.title('avg vs strike_rate')
# plt.xlabel('Average')
# plt.ylabel('Strike Rate')
# plt.show()

# Q4)
# tip = sb.load_dataset('tips')
# plt.scatter(tip['total_bill'],tip['tip'])
# plt.show()



# batsman = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\batsman_season_record.csv')
# print(batsman)
# plt.bar(np.arange(batsman.shape[0])-0.2,batsman['2015'],color='red',width=0.2)
# plt.bar(np.arange(batsman.shape[0]),batsman['2016'],color='blue',width = 0.2)
# plt.bar(np.arange(batsman.shape[0])+0.2,batsman['2017'],color='yellow',width = 0.2)
# plt.xticks(np.arange(batsman.shape[0]),batsman['batsman'],rotation = 90)
# plt.show()
# the graph show david warner was the most consistent



# Q6)
# batsman = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\batsman_season_record.csv')


# plt.bar(np.arange(batsman.shape[0]),batsman['2015'],color='red',width=0.2,label = '2015')
# plt.bar(np.arange(batsman.shape[0]),batsman['2016'],bottom=(batsman['2015']),color='blue',width = 0.2,label = '2016')
# plt.bar(np.arange(batsman.shape[0]),batsman['2017'],bottom=(batsman['2016']+batsman['2015']),color='yellow',width = 0.2,label = '2017')
# plt.xticks(np.arange(batsman.shape[0]),batsman['batsman'],rotation = 90)
# plt.legend()
# plt.show()
# batsman['total'] = (batsman[['2015','2016','2017']].sum(axis = 1))
# print(batsman)
# highest = batsman.loc[batsman['total'].idxmax(),['batsman','total']]
# print("Highest total runs:", highest['batsman'], "with", highest['total'])


# Q7)

# df = pd.read_csv('MatplotLib.py\\vk.csv')
# print(df)
# plt.hist(df['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100,110,120],width = 5,label='runs')
# plt.xlabel('runs')
# plt.ylabel('count of matches')
# plt.grid(True)
# plt.style.use('ggplot')
# plt.show()


# Q8)

# df = np.load('MatplotLib.py\\big-array.npy')
# plt.hist(df,log=True,width=5)
# plt.show()
# log makes it easy because if there are
# outliers it will make the graph 
# more readable because lograthmic concept
# is that 10-100 = 100-1000
# and linear logic is 10-20=20-30

# q9)

# df = pd.read_csv('MatplotLib.py\\gayle-175.csv')
# print(df)
# temp = np.zeros(df['batsman'].shape[0])
# x = df['batsman_runs'].idxmax()
# temp[x] = 0.2
# plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',explode=temp,shadow=True,colors=['brown','red','blue','green','yellow','pink'])
# plt.xticks(rotation = 90)
# plt.show()

# q10)

# df = pd.read_csv('MatplotLib.py\\sharma-kohli.csv')

# plt.style.use('fivethirtyeight')
# plt.bar(np.arange(df.shape[0]),df['RG Sharma'],color='blue',width = 0.2,label = 'RS')
# plt.bar(np.arange(df.shape[0])+0.2,df['V Kohli'],color = 'black',width=0.2,label = 'vk')
# plt.xlabel('years')
# plt.ylabel('runs')
# plt.legend()
# plt.xticks(np.arange(df.shape[0]),df['index'])
# plt.show()
