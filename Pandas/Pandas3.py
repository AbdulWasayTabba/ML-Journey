import pandas as pd
import numpy as np

subs = pd.read_csv('c:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\subs.csv').squeeze('columns')
# print(subs)

vk = pd.read_csv('c:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\kohli_ipl.csv',index_col='match_no').squeeze('columns')
# print(vk)

movies = pd.read_csv('c:\\Users\\HP\\Desktop\\datascienceNumpy\\Pandas\\bollywood.csv',index_col='movie').squeeze('columns')
# print(movies)


# Funtions

# astype
# import sys
# print(sys.getsizeof(vk))

# print(sys.getsizeof(vk.astype('int16')))


# between

# keh range keh andar value exist karte ya nahi

# print(vk[vk.between(51,99)].size)


# clip

# aik given range me clip kar deta
# e.g betwen 100 and 200 subs
# so all values below 100 will become and hundred and over 
# 300 will beomce 200

# print(subs.clip(100,200))


# drop_duplicates

# temp = pd.Series([1,1,2,2,3,3,4,4])
# print(temp)
# print(temp.drop_duplicates())
# print(temp.drop_duplicates(keep='last'))
# this will cause the first occurence to be deleted
# by default the first one dosent but keep causes that
# other wise dropduplicates just delets
# duplicate values


# duplicated()
# returns true or false
# true if duplicayed false if not
# print(vk.duplicated().sum())


temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
# size counts all the stuff
# count function counts the non null values
# print(temp.size)#10
# print(temp.count())#7


# isnull

# print(vk.isnull().sum())
# print(temp.isnull().sum())



# dropna

# removes all the missing values
# print(temp.dropna())


# fillna
# if you dont want to drop 
# print(temp.fillna(0))
# print(temp.fillna(temp.mean()))


# isin

# aik sath multiple cheezoon ko check karta hai
# in series

# print(vk[(vk == 49) | (vk == 99)])
# print(vk[vk.isin([49,99,69,79])])


# apply

# helps apply custom logic

# print(movies)
# if i want only the first name of the actor
# and the name should be fully capital

# print(movies.apply(lambda x:x.split()[0].upper()))

# print(subs)

# jin bhi din average se zyada sub 
# mean good and vice versa

# avg = subs.mean()
# print(subs.apply(lambda x:'good day' if x>avg else 'bad day'))


# copy

# print(vk)
# new = vk.head()
# new[1] = 100
# print(vk)
# this will cause chnage in the 
# orignal series thats why we 
# use copy so it dosent chnage the orignal series

# new = vk.head().copy()
# new[1] = 100
# print(new)
# print(vk)