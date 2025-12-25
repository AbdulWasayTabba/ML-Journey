# tricks parhe ge 
# functions and stuff

# 1)np.sort

import numpy as np


a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
# print(a)
# print(b)

#
# print(np.sort(a))
# 2d
# print(np.sort(b,axis=0)[::-1])
# 2d me row wise sorting kar raha
# agar column wise karna toh axis use karna 
# if descending order me karna use ::-1

# 2) np.append
# np.append(a,200)
# print(np.append(a,200))
# last me 200 agaya

# 2d

# print(np.append(b,np.ones((b.shape[0],1)),axis=1))
# agar last me aik column append karna cahte ho

# 3) np.concatenate
# joins arrays together

# c = np.arange(6).reshape(2,3)
# d = np.arange(6,12).reshape(2,3)
# print(c)
# print()
# print(d)

# print(np.concatenate((c,d),axis=1))#column
# print(np.concatenate((c,d),axis=0))#row
# alternate of np.vstack or np.hstack

# 4)np.unique
# 
# aik array se unique nikal kar ke de ga
# e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
# print(np.unique(e))
# sql ke distinct ke key word ke tarah hai

# 5)np.expand_dims
# e.g 1d ko 2d me convert kar sakhte 2d ko 3d..


# print(np.expand_dims(a,axis=1).shape)
# use to make row vector and column vector

# 6)np.where

# The numpy.where() function 
# returns the indices of 
# elements in an input array where the given condition is satisfied

# for example un sare items ka index potion chaiye
# jo 50 se zyada hai
# print(a)
# print(np.where(a>50))

# another use

# replace all values who are greater than 50
# np.where(condition,true,false)
# print(np.where(a>50,0,a))

# replace even with 0
# print(np.where(a%2==0,0,a))

# replace odd
# print(np.where(a %2 == 1,1,a))

# 7)np.argmax 

# returns index of max value

# print(a,np.argmax(a))

# 2d
# print(b,np.argmax(b,axis=0))
# axis define karna ho ga


# 8)np.argmin

# opposite of np.argmax

# 9)np.cumsum

# cummulative sum

# cumulative sum 

# print(a,np.cumsum(a))

# e.g
# [73 73 13 16 67 53 89 65 29 93  4 28 56 15 95]
#  [ 73 146 159 175 242 295 384 449 478 571 575 603 659 674 769]

# 2d
# print(b,np.cumsum(b,axis=0))


# 10)np.cumprod

# same as sumsum the only diff is 
# that instead of adding it multiplies


# 11)np.precentile

# used to computed the nth percentile of the given 
# data

# eg in a paper agar 50 percent aya toh
# uska matlab 50% log behter hai usse aur 49% worse
# print(a)
# print(a,np.percentile(a,50))

# print(b,np.percentile(b, 50))


# 12)np.histogram

# frequency count in a given range

# 5 15 9 17 25 23 29
# bin size = 10(0-10)(11-20)(21_30)
# now we find pehel ke 0 se 10 ke beech me kitne 
# num hai and so one 
# 0-10 =2 
# 11-20 = 2

# print()
# print(a,np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))

# 13)np.corrcoef

# koi bhi do quantities kitne co related hai
# e.g experience aur salary

# salary = np.array([20000,40000,25000,35000,60000])
# experience = np.array([1,3,2,4,2])

# print(np.corrcoef(salary,experience))

# 14)np.isin

# searches multiple items in a array like in in sql
# items = [10,20,30,40,50]
# print(a,np.isin(a,items))
# keh a me items exist karte hai ya nahi
# print(a,a[np.isin(a,items)])
# bolean masking wale techniwue hai 
# is se jo values mile hai woh print ho jaye ge

# 15)np.flip

# reverse
# but will maintian the shape
# print(a,np.flip(a))

# 2d

# print(b,'\n\n',np.flip(b))#fliiping both
# print(b,'\n\n',np.flip(b,axis=0))#column flipping
# print(b,'\n\n',np.flip(b,axis=1))#row flipping

# 16 )np.put
# The numpy.put() function replaces
#  specific elements of an array with given
#  values of p_array. Array indexed
#  works on flattened array.

# print(a,'\n',np.put(a,[0,1],[101,503]))
# print(a)
# change multiple items in existing places

# 17)np.delete

# The numpy.delete() function returns 
# a new array with the deletion of
#  sub-arrays along with the mentioned axis.

# print(np.delete(a,0))
# print(a)

# 18)set function

# np.union1d
# np.intersect1d
# np.setdiff1d
# np.setxor1d
# np.in1d

# m = np.array([1,2,3,4,5])
# n = np.array([3,4,5,6,7])

# np.union1d(m,n)

# np.intersect1d(m,n)#matching 
# np.setdiff1d(n,m)#woh sare jo m me hai aur n me sahi
# np.setxor1d(m,n)#common ko hata de ga
# m[np.in1d(m,1)]#search karta keh m me 1 hai ya nahi

# 19)np.clip
# aik range me values ko rakhta hai
# print(a)
# print(np.clip(a,a_min=25,a_max=75))







