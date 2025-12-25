# List


# What are Lists?
# Lists Vs Arrays
# Characterstics of a List
# How to create a list
# Access items from a List
# Editing items in a List
# Deleting items from a List
# Operations on Lists
# Functions on List


# What are Lists
# List is a data type where you can
# store multiple items under 1 name.
# More technically, lists act like dynamic
# arrays which means you can add more items 
# on the fly.


# Array Vs Lists
# Fixed Vs Dynamic Size
# Convenience -> Hetrogeneous(multiple data types)
# Speed of Execution
# Memory

# arrays store kese hote hai ?
# int arr[50]
# in memory you make continious blocks
# woh block me value jo store hote
#  hai woh binary me hote hai

# list kese store hota hai
# list [1,2,3]
# [1] [2]  [3]
# 500 600 700
# 1001 1002 1003
# jo one value hai woh 500 address 
# pe store hote aur woh 500 
# ka bhi adress hota 1001 

# this is called 
# referntial array
# beacuse you storing the address

# id() function prints the memory address 

# a = 2
# print(id(a))#dono ka memory adress
# print(id(2))#same hai

# L = [1,2,3]
# print(id(L))
# print(id(L[0]))
# print(id(L[1]))
# print(id(L[2]))
# print(id(1))
# print(id(2))
# print(id(3))

#  the memory address of 
# L[0] = 1 
# beacuse on L[0] there is 1

# so since you are storing 
# addresses in list
# you can then store diffrent data tyoes
# in the same list 
# beacuse you arent breaking any rules
# the rule is to store a address

# + list is a dynamic array
# it starts with a fixed array at first
# then double the array until 
# the requirments exeeds the current 
# space then you double again and keep
# on repeating hence dynamic array

# so as you can see because of these 
# process it takes more time 
# and memory
# but it is more convienient


# Characterstics of a List
# Ordered([1,2,3] is not equal to [3,2,1])
# Changeble/Mutable
# Hetrogeneous
# Can have duplicates
# are dynamic
# can be nested(list ke andar aik list dal sakhte ho)
# items can be accessed
# can contain any kind of objects in python


# creating  a list

# empty
# print([])

# 1D
# print([1,2,3,4,5])#homegeneous to 
# because all data types are same

# 2D
# print([1,2,3,[4,5]])#hetrogenous

# 3D
# print([[[1,2],[3,4]],[[5,6],[7,8]]])

#hetrogenous
# print([1,True,5.6,5+6j,'hello'])

# using type conversion
# print(list('hello'))



# Accessing items from a list

#indexing
# L = [1,2,3,4,5]
# L1 = [1,2,3,[4,5]]
# L2 = [[[1,2],[3,4]],[[5,6],[7,8]]]
#postive indexing:left se right starts with 0
# print(L[0])
# print(L1[3][0])
# print(L2[0])
# print(L2[1][0][0])#5
# print(L2[0][1][0])#3
# print(L2[0][0][1])#2

#negative indexing:right to left startes with -1
# print(L[-1])
# print(L1[-1])
# print(L1[-1][-2])


#slicing

# extracting multiple items
# L = [1,2,3,4,5,6]

# print(L[0:3])
# print(L[-3:])
# print(L[0::2])
# # negative
# print(L[-5:-2:2])
# print(L[::-1]) #reverse


# adding items to a list

# append
# extend
# insert

# append:aik bar aike item ko list

# ke end me add kar deta
# L = [1,2,3,4,5]
# L.append(7)
# print(L)

# extend:aik sath multiple items ko add kar
# sakhte ho

# L = [1,2,3,4,5]
# L.extend([6,7,8])
# print(L)

# insert: postion ke liye hai
# apne desired location

# L = [1,2,3,4,5]
# L.insert(1,100)#POSTION THEN VALUE 
# print(L)

# Editing items in a List

# editing with indexing
# L = [1,2,3,4,5]
# # if i wanna make 5 500
# L[-1] = 500
# print(L)

# editing with slicing
# L = [1,2,3,4,5]
# # change 2 3 and 4
# L[1:4] = [200,300,400]
# print(L)



# Deleting items from a List

# del

# L = [1,2,3,4,5]
# print(L)
# del L #deletes the whole list not on 
# memory level though
# print(L)

# indexing
# L1 = [1,2,3,4,5]
# del L1[-1]
# print(L1)

# slicing
# L1 = [1,2,3,4,5]
# del L1[1:4]
# print(L1)


# remove

# item ko value ke hisab se delete kar 
# sakhte ho
# L = [1,2,3,4,5]
# L.remove(5)
# print(L)


# pop 
# particular index wale item ko delete karta
# warna if index not defined will delete the 
# last item
# L = [1,2,3,4,5]
# L.pop(0)
# L.pop()
# print(L)


# clear
# deletes all items
# makes a empty list

# L = [1,2,3,4,5]
# L.clear()
# print(L)

# Operators on List

# Arthmetic
# memebership
# Loop

# Arthmetic(+,*)

# L1 = [1,2,3,4]
# L2 = [5,6,7,8]
# # concatenate/Merge
# print(L1+L2)
# print(L1*3)

# Membership

# L1 = [1,2,3,4,5]
# L2 = [1,2,3,4,[5,6]]
# print(5 in L1)#asking keh L1 me 5 hai ?
# print(5 in L2)#False


# Loops


# L1 = [1,2,3,4,5]
# L2 = [1,2,3,4,[5,6]]
# L3 = [[[1,2],[3,4],[5,6],[7,8]]]
# for i in L1:
#     print(i)
# for i in L2:
#     print(i)
# for i in L3:
#   print(i)


# List Functions

# len/min/max/sorted
# L = [2,1,5,7,0]
# print(len(L))
# print(min(L))
# print(max(L))
# print(sorted(L))

# count
# L = [1,2,1,3,4,1,5]
# print(L.count(1))

# index
# tells index postiion

# L = [1,2,1,3,4,1,5]
# print(L.index(5))#5 ka index pos 6 hai


# reverse 

# L = [1,2,1,3,4,1,5]
# L.reverse() #permanently reverses the list
# print(L)


# sort

# L = [1,2,1,3,4,1,5]
# print(L)
# print(sorted(L))
# print(L)
# L.sort()
# print(L)

#this show keh sort() permanently 
# sort karta hai ulike sorted

# copy

# L = [1,2,1,3,4,1,5]

# print(L)
# print(id(L))
# L1 =L.copy()#makes a shallow copy
# # with diffent address
# print(L1)
# print(id(L1))


# List comprehension


# List Comprehension provides a concise way of creating lists.

# newlist = [expression for item in iterable if 
#            condition == True]

# Advantages of List Comprehension

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.

#   Add 1 to 10 numbers to a list

# L = []
# for i in range(1,11):
#     L.append(i)
# print(L)#yeh 4 lines ka hai 

# L = [i for i in range(1,11)]#same thing in 1 line
# print(L)


# scalar multiplication on a vector

# v = [2,3,4]
# s = -3
# # [-6,-9,-12]
# x = []
# for i in v:
#     x.append(i*s)

# so instead of this

# L = [s*i for i in v]
# print(L)

# Squares

# L = [i**2 for i in range(1,6)]

# print(L)


# print all numbers divisible by 5 in the range of 
# 1 to 50

# L = [i for i in range(1,51) if i %5 == 0]
# print(L)

# find lanaguage which start with the letter p

# L = ['java','python','php','c','javascripy']
# print([i for i in L if i.startswith('p') ])


# Nested if with List Comprehension

# basket = ['apple','gauava','cherry','banana']
# my_fruits=['apple','kiwi','grapes','banana']
# add new list from my_fruits and items if the fruit exists in 
# basket and also starts with 'a'

# L = [i for i in my_fruits if i in basket if i.startswith('a')]
# print(L)



# print a (3,3) matrix using list
#  comprehension->nested list comprehension

# print([[i*j for i in range(1,4)] for j in range(1,4) ])

# catesian products -> List comprehension on 2 lists together

# L1 = [1,2,3,4]
# L2 = [5,6,7,8]
# print([i*j for i in L1 for j in L2])




# 2 ways to traverse a list

# itemwise
# indexwise


# itemwise
# L = [1,2,3,4]
# for i in L:
#     print(i)


# indexwise

# L = [1,2,3,4]
# for i in range(0,len(L)):
#     print(L[i])



# zip function


# The zip() function returns a zip object
# , which is an iterator 
# of tuples where the first item in each passed 
# iterator is paired together, and
# then the second item in each passed 
# iterator are paired together.
# If the passed iterators have different 
# lengths, the iterator with the least items 
# decides the length of the new iterator.


# write a program to add items of 2 lists

# l1=[1,2,3,4]
# l2=[-1,-2,-3,-4]

# print(list(zip (l1,l2)))
# print([i+j for i,j in zip(l1,l2)])


# python list can store any kind of object 

# l = [1,2,print,type,input]
# print(l)#error nahi throw kare ga 




