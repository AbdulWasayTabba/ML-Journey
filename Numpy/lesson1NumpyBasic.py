# numpy main cheez hai ndarray
# isme it is faster
# same data type and fixed size
# unlike python lists
# used in pandas matlab ml
#for scientific calculations

import numpy as np

# a= np.array([1,2,3])
# print(type(a))
# print(a)

# 2d

# b = np.array([[1,2,3],[4,5,6]])
# print(b)

# 3d
# c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c)

# datatype
# a = np.array([0,2,3],dtype=bool)
# print(a)

# np.arange

# a = np.arange(1,11,2)
# print(a)

# arange is used with reshape
# reshape(rows,columns)
# a = np.arange(1,11).reshape(5,2)
# print(a)

# np.ones and np.zeros
# on the go aik array bana sakhte ho jiske sare ke sare
# array ke values 1 ya 0 hoye

# a= np.ones((3,4))#this is also reshaping it in 3 rows and 4 columns
# print(a)

# a = np.random.random((3,4))
# print(a)

# np.linspace is linear space 
# np.linspace(startrange,endrange,numofitems)
# equal distance hoye ga 2 point ke beech me 
# when using this method
# linearly seperable points genrate kara hai in a given range

# a = np.linspace(25,100,4)
# print(a)

# np.identity
# generates identity matrix

# a  = np.identity(3)
# print(a)

# this was numpy arrays creation


# now numpy attributues



# a1 = np.arange(10)
# a2 = np.arange(12,dtype=float).reshape(3,4)
# a3 = np.arange(8).reshape(2,2,2)

# ndim
#number of dimensions

# print(a1)
# print(a1.ndim)
# print(a2)
# print(a2.ndim)
# print(a3)
# print(a3.ndim)


#shape
# har dimensions me kitne items hai

# print(a1.shape)
# print(a2.shape)
# print(a3.shape)
# to read 3d ka pehla wala tells you keh kitne 2d arrays hai

# size
# number of items

# print(a1.size)
# print(a2.size)
# print(a3.size)

# itemsize
# har item memory me kitna size occupy kar raha hai

# print(a1.itemsize)
# print(a2.itemsize)
# print(a3.itemsize)

# dtype
# type of value

# print(a1.dtype)


# changing data types

# astype
# used to save memory sometimes 
 
# print(a3.dtype)
# a3.astype(np.int32)
# print(a3.dtype)



# Array operations



# a1 = np.arange(12).reshape(3,4)
# a2 = np.arange(12,24).reshape(3,4)

#scalar operations

#arthimetic

# print(a1* 2)

# print(a1/ 2)

# print(a1- 2)

# print(a1+ 2)

# print(a1** 2)

# # relational

# print(a2>15)

# print(a2==15)

# print(a2!=15)

# vector operations
# in vector you apply operations on 2 arrays or more
# shape should be same

# arthimetic

# print(a1+a2)

# Array Functions

# a1 = np.random.random((3,3))
# print(a1)
# a1= np.round(a1*100)
# print(a1)

# print(np.max(a1))
# print(np.min(a1))
# print(np.prod(a1))
# print(np.sum(a1))

# if har row ka min chaiye then
# axis identifier hai row aur column ke liye
# print(np.min(a1,axis=1))  #0 -> col 1 -> row
# print(np.max(a1,axis=0)) 
# print(np.sum(a1,axis=1)) 
# print(np.prod(a1,axis=1)) 

# statistical funtions

# print(np.mean(a1,axis=1))
# print(np.median(a1,axis=1))
# print(np.var(a1,axis=1))

# trignometric function
# print(np.sin(a1))

# dot product
# dot product do matrix multiply 
# pehle wale matrix ka column and dosre ka row match hona chaye
# (3,4),(4,3)

# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(12,24).reshape(4,3)
# print(a2)
# print(a3)
# print(np.dot(a2,a3))




# logs and exponents
# print(np.log(a1))
# print(np.exp(a1))

# round/floor/ceil

# a3 = np.round(np.random.random((2,3))*100)
# print(a3)
# a3 = np.ceil(np.random.random((2,3))*100)
# print(a3)
# a3 = np.floor(np.random.random((2,3))*100)
# print(a3)

# Indexing and slicing
# 

# npmy array hai toh ap fetch kar sakhte ho item ko using indexing

# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(27).reshape(3,3,3)

# 1d

# print(a1)
# print(a1[-1])

# 2d

# print(a2)
# print(a2[1,2])#to find 6
# print(a2[1,0])#for 4

# print(a3)
# print(a3[0,2,0])# for 6 in a3
# print(a3[0,0,0])#for 0 in a3
# print(a3[0,1,2])# for 5 in a3
# i wrote 0 first because 6 was in the fist 2d array in the 3d array
# then 2 because of row then  0 because of column
# so you have to understand that 3d is made up of 2ds and 
# 2ds is made up of 1ds


# now slicing 
# in indexing we fetch one item 
# but in slicing we can fetch multiple items

# 1d

# print(a1)
# print(a1[2:5])
# print(a1[2:5:2])


# 2d

# print( a2)
# print(a2[0,:])
# print(a2[:,2])
# print(a2[1:,1:3])
# print(a2[::2,::3])
# print(a2[::2,1::2])
# print(a2[1,::3])
# print(a2[0:2,1:])
# print(a2[1:,0:2])
# print(a2[::2,0:2])

# 3d
# print(a3)
# print(a3)
# print(a3[1,::])
# print(a3[::2])
# print(a3[0,1,:])
# print(a3[1,:,1])
# print(a3[2,1:,1:])
# print(a3[::2,0,::2])

# print(a1)
# for i in a1: 
#  print(i)

# print(a2)
# for i in a2:
#    print(i)

# print(a3)
# for i in a3:
#    print(i)   

#    agar specific pe loop run karna

# for i in np.nditer(a3):
#    print(i)

#    this converted the 3d to 1d then printed them


# Reshaping

# reshape jo pehle kara tha

# transpose
# row ka coloumn aur column ko row


# print(a2)
# print(np.transpose(a2))


# ravel
# converts  to 1d

# print(np.ravel(a3))

# Stacking


# you can join nmpy arrays horizontally or vertically


# a4 = np.arange(12).reshape(3,4)
# a5 = np.arange(12,24).reshape(3,4)

# print(a4)
# print(a5)

# print(np.hstack((a4,a5)))

# print(np.vstack((a4,a5)))


# if you have mutiple soucres of data
# and you want to analyse them together then you apply this
# the size or the arrays should be same


# Splitting
# opposite of stacking

# print(np.hsplit(a4,4))
# print(np.vsplit(a4,3))