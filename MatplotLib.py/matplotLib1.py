# Fundementals of matplotlib
# Types of data 

# Numerical data = age,weight,temperature
# Categorical data = phone brand,college branch, gender

# import the library
from turtle import color, width
from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# single pe plot karte ho 
# univariat
# 2 columns = bivariat
# more than 2 = multivariat

# 2d Line Plot

# 2d line plot is used for bivairat
# analysis
# e.g product sales me app
# sales amount and months yeh two 
# colums pe 
# usually aik column numerical hai
# aur doosra column categorical hai

# Bivariate Analysis
# categorical -> numerical and numerical -> numerical
# Use case - Time series data


# Plotting a simple function

# price = [48000,54000,57000,49000,47000,45000]
# years = [2015,2016,2017,2018,2019,2020]

# plt.plot(years,price)
# plt.show()
# pehla paramereter is on the x axis the second one is y axis
# in this case years is on x axis and price is on y axis

batsman = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\sharma-kohli.csv')
# print(batsman)

# plt.plot(batsman['index'],batsman['V Kohli'])
# plt.plot(batsman['index'],batsman['RG Sharma'])
# plt.show()
# if we want to compare kohli and sharam trakc record


# to make the graph more clean we do this
# labels title
# plt.plot(batsman['index'],batsman['V Kohli'])
# plt.plot(batsman['index'],batsman['RG Sharma'])
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.show()



# colors(hex)
# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green')
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black')
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.show()


# line(width and style)

# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green',linestyle='dashed')
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black',linestyle = 'dashed')
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.show()


# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green',linestyle='dotted')
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black',linestyle = 'dotted')
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.show()

# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green',linestyle='solid',linewidth = 3)
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black',linestyle = 'dashdot',linewidth = 2)
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.show()


# markers(size)

# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green',linestyle='solid',linewidth = 3,marker = 'D',markersize = 9)
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black',linestyle = 'dashdot',linewidth = 2,marker = 'D',markersize = 9)
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.show()
# D is for Diamond in marker
# +
# .
# >
# <
# o circle


# ab the ques is which color line is which batsmans
# vk or sharma

# label
# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green',linestyle='solid',linewidth = 3,marker = 'D',markersize = 9,label = 'Virat')
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black',linestyle = 'dashdot',linewidth = 2,marker = 'D',markersize = 9,label = 'Sharma')
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.legend(loc = 'uppper right')
# plt.show()
# plt legend help in specifying which is for what
# and its default location is best which is 
# top left

# if i want the labeling of the line color = player
# on the right side instead of the left you cagne loc

# these are all of the options

# for loc 

# ' right' is not a valid value for loc;
# supported values are 'best', 'upper right', 
# 'upper left', 'lower left', 'lower right', 
# 'right', 'center left', 'center right', 
# 'lower center', 'upper center', 'center'


# limitng axis


# price = [48000,54000,57000,49000,47000,45000,450000]
# years = [2015,2016,2017,2018,2019,2020,2021]

# plt.plot(years,price)
# plt.show()
# isme last wale value is too high comapred to 
# the other so it is a outlier
# that is causing the other values in the graph
# to be in a single line
# so in this scenario you can do trimmign in the graph 

# plt.ylim()
# price = [48000,54000,57000,49000,47000,45000,450000]
# years = [2015,2016,2017,2018,2019,2020,2021]

# plt.plot(years,price)
# plt.xlim(2017,2020)
# plt.ylim(0,70000)
# plt.show()
# ylime is basically range 
# it is saying that range 0 se 70000 tak dekhao
# aise he x axis me bhi hota
# plt.xlim()

# you do this when there are outliers in the data

# plt.grid()
# better readability

# plt.plot(batsman['index'],batsman['V Kohli'],color = 'green',linestyle='solid',linewidth = 3,marker = 'D',markersize = 9,label = 'Virat')
# plt.plot(batsman['index'],batsman['RG Sharma'],color = 'black',linestyle = 'dashdot',linewidth = 2,marker = 'D',markersize = 9,label = 'Sharma')
# plt.title('Rohit Sharma vs V Kohli Comparision')
# plt.xlabel('Season')
# plt.ylabel('Runs Scored')
# plt.legend(loc = 'best')
# plt.grid()
# plt.show()




# Scatter Plot

# Bivariate Analysis
# numerical vs numerical
# Use case - Finding correlation between two quantities


# plt.scatter simple functionm

# x = np.linspace(-10,10,50)
# print(x)
# y = 10*x + 3 + np.random.randint(0,300,50)
# print(y)
# plt.scatter(x,y)
# plt.show()

# plt.scatter on pandas data

df = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\batter.csv')
# print(df)
# from this we will take out top 50 batsman
# then use scatter and on the x axis avg
# y axis strike rate 
# top50 = df.head(50)
# plt.scatter(top50['avg'],top50['strike_rate'],color = 'red')
# plt.title('Avg and DR analysis of top 50 Batsman')
# plt.xlabel('avg')
# plt.ylabel('Strike Rate')
# plt.show()


# size
tips = sns.load_dataset('tips')

# plt.scatter(tips['total_bill'],tips['tip'],s=tips['size']*20)
# plt.show()
# s=tips['size'] yeh wala kya kar raha
# yeh bol raha keh agar size bara ho ga
# toh scatter plot me woh itna bara hoye ga

# yeh wala scatter plot 3 dimensions me 
# info print kara
# total bill tip and size 

# scatterplot using plt.plot instead of plt.scatter

# plt.plot(tips['total_bill'],tips['tip'],'o')
# plt.show()
# you can do this
# because it if fastetr than plt.scatter
# but if you need to use color size
# then use scatter 





# Bar Chart

# Bivariate Analysis
# Numerical vs Categorical
# Use case - Aggregate analysis of groups


# simple bar chart

children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']
# plt.bar(color,children,color = 'black')
# plt.show()

# horizontal bar chart
# plt.barh(colors,children,color='black')
# plt.show()

# color and labels 
# same way as in plot and scatter

df = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\batsman_season_record.csv')

# ques = batsman ne 2015 me kitne runs banaye
# plt.bar(df['batsman'],df['2015'])
# plt.show()
# then somone says side by side 2016 ka bhi bano

# plt.bar(df['batsman'],df['2015'])
# plt.bar(df['batsman'],df['2015'])
# plt.show()
# this show that only ms dhoni
# from all the batsman made less in 2016 compared to 2015

# /but this isnt very readable
# its better to have them side by side 
# instead of them overlapping each other

# plt.bar(np.arange(df.shape[0]) - 0.2,df['2015'],width=0.2,color='yellow')
# plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2,color='red')
# plt.bar(np.arange(df.shape[0]) + 0.2,df['2017'],width=0.2,color='blue')
# plt.show()

# issme batsman ka name nahi dekh raha
# so we use plt.xticks
# we provide existing labels and wjat to replace it with

# plt.bar(np.arange(df.shape[0]) - 0.2,df['2015'],width=0.2,color='yellow')
# plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2,color='red')
# plt.bar(np.arange(df.shape[0]) + 0.2,df['2017'],width=0.2,color='blue')
# plt.xticks(np.arange(df.shape[0]),df['batsman'])
# plt.show()



# problem
# a problem
# children = [10,20,40,10,30]
# colors = ['red red red red red red','blue blue blue blue','green green green green green','yellow yellow yellow yellow ','pink pinkpinkpink']

# plt.bar(colors,children)
# plt.show()

# isse category over lap ho rahe  so we use 
# xticks here too

# children = [10,20,40,10,30]
# colors = ['red red red red red red','blue blue blue blue','green green green green green','yellow yellow yellow yellow ','pink pinkpinkpink']

# plt.bar(colors,children)
# plt.xticks(rotation = 'vertical')
# plt.show()
# aise sare names vertically dekh rahe and they 
# arent overlapping


# Stacked bar chart
# basically multiple bar connected to each other


# plt.bar(df['batsman'],df['2017'],label='2017')
# plt.bar(df['batsman'],df['2016'],bottom=df['2017'],label='2016')
# plt.bar(df['batsman'],df['2015'],bottom=(df['2016'] + df['2017']),label='2015')

# plt.legend()
# plt.show()



# plt.bar(df['batsman'],df['2017'],bottom=(df['2016']+df['2015']),label='2017')
# plt.bar(df['batsman'],df['2016'],bottom=df['2015'],label='2016')
# plt.bar(df['batsman'],df['2015'],label='2015')

# plt.legend()
# plt.show()

# basically bottom  use karo ge keh
# for e.g 2017 keh bottom pe 2015 + 2016
# 2016 ke neeche 2015
# 2015 ke neeche nothing


# Histogram


# Univariate Analysis
# Numerical col
# Use case - Frequency Count



# data = [32,45,56,10,15,27,61]

# plt.hist(data,bins=[10,25,40,55,70],width=6)
# plt.show()

# handinling bins on real data set

# df = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\vk.csv')

# plt.hist(df['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
# plt.show()



# logarithmic scale

# arr = np.load('MatplotLib.py\\big-array.npy')
# plt.hist(arr)
# plt.show()
# it created it own bins 
# but the problem is that 
# that there are so many numbers in some bins
# the bins look like nothing
# so rather than using a linear
#  scale we can use a lograthimic scale

# log scale logic
# 1-100 = 100-1000
# linear logic 
# 1-2 = 2-3

# arr = np.load('MatplotLib.py\\big-array.npy')
# plt.hist(arr,bins=[0,10,20,30,40,50,60,70],log = True)
# plt.show()






# Pie Chart

# Univariate/Bivariate Analysis
# Categorical vs numerical
# Use case - To find contibution on a standard scale

# simple data
# data = [23,45,100,20,49]
# subjects = ['eng','science','maths','sst','hindi']
# plt.pie(data,labels=subjects)
# plt.show()


# dataset

# df = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\gayle-175.csv')
# plt.pie(df['batsman_runs'],labels=df['batsman'])
# plt.show()
# to show percentage contribution
# parameter =  autopct
# df = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\gayle-175.csv')
# plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%')
# plt.show()


# percentage and colors
df = pd.read_csv('C:\\Users\\HP\\Desktop\\datascienceNumpy\\MatplotLib.py\\gayle-175.csv')
# plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',colors=['blue','green','yellow','pink','cyan','brown'])
# plt.show()

# explode shadow
# plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',explode=[0.1,0,0,0.1,0,0],shadow=True)
# plt.show()
# tab karte when you want to focus on a 
# particular category


# shadow gives a 3d feel



# Changing styles

# print(plt.style.available)
# diffrent styles in matplotlib


# plt.style.use('fivethirtyeight')
# to apply a style



# arr = np.load('MatplotLib.py\\big-array.npy')
# plt.hist(arr,bins=[0,10,20,30,40,50,60,70],log = True)
# plt.show()


# agar graph ko save kare ke export karna

# arr = np.load('MatplotLib.py\\big-array.npy')
# plt.hist(arr,bins=[0,10,20,30,40,50,60,70],log = True)
# plt.savefig('sample.png')
# you save it without using plt.show

# check doc on website