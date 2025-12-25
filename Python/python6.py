# Tuples
# A tuple in Python is similar to a list. 
# The difference between the two is that 
# we cannot change the elements of a tuple
#  once it is assigned(immutable)
#  whereas we can change
#  the elements of a list.

# In short, a tuple is an immutable list.
#  A tuple can not be changed in any way 
# once it is created.

# Characterstics

# Ordered
# Unchangeble
# Allows duplicate
# Plan of attack
# Creating a Tuple
# Accessing items: POSSIBLE
# Editing items: NOT POSSIBLE
# Adding items: NOT POSSIBLE
# Deleting items: possible but only whole tuple not a portion
# Operations on Tuples
# Tuple Functions

# Creating Tuples

# t1 = ()
# print(t1)

# create a typle with a single item

# t2 = ('hello',)#the comma is neccasry for a single 
# # item tuple
# print(t2)

# # homogenous tuple same data type
# t3 = (1,2,3,4)
# print(t3)
# # hetrogenous tuple diffrent data type
# t4 = (1,True,[1,2])
# print(t4)
# # nested tuple
# t5 = (1,2,3,(4,5))
# print(t5)

# # using type conversion
# t6 = tuple('hello')
# print(t6)

# Accessing items

# indexing and slicing 

# indexing

# print(t3[0])
# print(t3[-1])
# print(t5[-1][-1])

# slicing

# print(t3[0:4:2])
# print(t3[::-1])
# print(t5[2:4])

# Editing Items

# t3 = (1,2,3,4)
# t3[0] = 100
# not possible because immutable like strings
#toh editing hota he nahi 

# Adding items

#not possible


# deleting items

# you can only delete the whole
#  tuple not a potion of it

# t3 = (1,2,3,4)
# print(t3)
# del t3
# print(t3)

# operation on tuples

# + and *

# t1 = (1,2,3,4)
# t2 = (5,6,7,8)
# print(t1+t2)
# print(t1*3)

# membership

# print(1 in t1)

# # loop
# for i in t1:
#     print(i)


# len/sum/min/max/sorted
# t = (1,2,3,4)
# len(t)

# sum(t)

# min(t)

# max(t)

# sorted(t,reverse=True)


# count

# print(t.count(1))


# index

# print(t.index(50))


# Difference between Lists and Tuples
# Syntax
# Mutability
# Speed(tuples are faster than list)
# Memory(tuple takes lesser memory comapred to list)
# Built in functionality
# Error prone(list is more error prone)
# Usability

# import time 

# L = list(range(100000000))
# T = tuple(range(100000000))

# start = time.time()
# for i in L:
#   i*5
# print('List time',time.time()-start)

# start = time.time()
# for i in T:
#   i*5
# print('Tuple time',time.time()-start)

# this proves speed ka difference

# import sys

# L = list(range(1000))
# T = tuple(range(1000))

# print('List size',sys.getsizeof(L))
# print('Tuple size',sys.getsizeof(T))

# this proves memory ka difference


# a = [1,2,3]
# b = a

# a.append(4)
# print(a)
# print(b)

# error prone zyada hai list

# a = (1,2,3)
# b = a

# a = a + (4,)
# print(a)
# print(b)

# Special syntax

# tuple unpacking

# a,b,c = (1,2,3)
# print(a,b,c)

# swap values in python

# a = 1
# b =2
# a,b = b,a
# print(a,b)

# agar khali 2 values chaiye 

# a,b,*others = (1,2,3,4)
# print(a,b)
# print(others)


# zip functions

# a = (1,2,3,4)
# b = (5,6,7,8)
# print(tuple(zip(a,b)))

# tuple comprehension hota hai

# t = (i for i in range(1,11,2))
# print(t)#you cant just print like this because 
# tuple dosent store all the values it uses 
# a genrator so you have to run a loop to 
# print the values

# t = (i for i in range(1,11,2))
# for i in t:
#     print(i)

# or

# t = tuple(i for i in range(1, 11, 2))
# print(t)


# Sets

# A set is an unordered collection of items. 
# Every set element is unique (no duplicates)
# and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add
# or remove items from it.

# Sets can also be used to perform mathematical
# set operations like union, intersection, 
# symmetric difference, etc.

# Characterstics:

# Can't contain mutable data types
# Unordered
# Mutable
# No Duplicates

# Creating Sets {}

# empty
# s = set()
# print(s)
# print(type(s))
# # 1D and 2D
# s1 = {1,2,3}
# print(s1)
#s2 = {1,2,3,{4,5}}
#print(s2)#not possible because 
# a set is a mutable data type

# # homo and hetro
# s3 = {1,'hello',4.5,(1,2,3)}
# print(s3)
# the order is decided by hashing


# using type conversion

# s4 = set([1,2,3])
# print(s4)
# duplicates not allowed
# s5 = {1,1,2,2,3,3}
# print(s5)
# set can't have mutable items
# s6 = {1,2,[3,4]}
# print(s6)

# s1 = {1,2,3}
# s2 = {3,2,1}

# print(s1 == s2)
# answer true aye ga 
# because unordered hota 
# hai so it checks the content
# not position

# Accessing Items

# s1 = {1,2,3,4}
# s1[0:3]

# not possible because it is 
# unordered
# so slicing and 
# indexing isnt possible 
# for sets

# Editing Items

# s1 = {1,2,3,4}
# s1[0] = 100
# not possible

# Adding items 

# s = {1,2,3,4}
# s.add(5)
# print(s)
# possible hai

# update:adds multiple items 
# s.update([5,6,7])
# print(s)


# Deleting items

# del
# poore set ko delete kar sakhte

# s = {1,2,3,4}
# print(s)
# del s 
# print(s)

# discard
# ap batae ho konse item ko 
# delete karna hai

# s = {1,2,3,4}
# s.discard(5)
# print(s)

# remove 
# same as discard

# s = {1,2,3,4}
# s.remove(5)
# print(s)
# the only diff is keh 
# discard wont throw a error
# when deleting something that
# dosent exist 
# but remove will

# pop
# deletes any item randomly
# ya phir smallest value ko i think

# s = {2,1,3,4}
# s.pop()
# print(s)

# clear

# empty kar deta set ko 

# s = {2,1,3,4}
# s.clear()
# print(s)

# Set Operations

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1 | s2)
# # Union(|)
# # Intersection(&)
# print(s1 & s2)
# # Difference(-)
# print(s1 - s2)
# print(s2 - s1)
# # Symmetric Difference(^)
# print(s1 ^ s2)
# # Membership Test
# print(1 not in s1)
# # Iteration
# for i in s1:
#   print(i)



# Set functions


# len/sum/min/max/sorted
# s = {3,1,4,5,2,7}
# len(s)
# sum(s)
# min(s)
# max(s)
# print(sorted(s,reverse=True))
#sorted function ka answer hamesha list me ata

# union/update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# #s1|s2
# s1.union(s2)#same answer

# s1.update(s2)
# print(s1)
# print(s2)

# intersection/intersection_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s1.intersection(s2)

# s1.intersection_update(s2)
# print(s1)
# print(s2)


# difference/difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s1.difference(s2)

# s1.difference_update(s2)
# print(s1)
# print(s2)


# symmetric_difference/symmetric_difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s1.symmetric_difference(s2)

# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)



# isdisjoint/issubset/issuperset
# s1 = {1,2,3,4}
# s2 = {7,8,5,6}

# print(s1.isdisjoint(s2))
# disjoint sets jin me aik bhi 
# item common nahi hota

# issubset
# s1 = {1,2,3,4,5}
# s2 = {3,4,5}

# s2.issubset(s1)
# true because s2 is inside s1


# issuperset
# s1 = {1,2,3,4,5}
# s2 = {3,4,5}

# s1.issuperset(s2)


# copy

# creates a shallow copy

# s1 = {1,2,3}
# s2 = s1.copy
# print(s1)
# print(s2)

# Frozenset

# Frozen set is just an immutable 
# version of a Python set object

# what works and what does not
# works -> all read functions
# does't work -> write operations



# create frozen_sets
# fs1 = frozenset([1,2,3])
# fs2 = frozenset([4,5,6])
# print(fs1 | fs2)

# When to use
# when you are making a
# ready only operations chalana chate ho
# aur chnages nahi hoye

# 2D sets
# fs = frozenset([1,2,frozenset([3,4])])
# print(fs)
# possible unlike normal set
# because frozenset is a imutable object


# Set comprehension

# 1 to 10

# s1 = {i for i in range(1,11)}
# print(s1)

# s2 = {i**2 for i in range(1,11) if i >5}
# print(s2)



# Dictionary
# Dictionary in Python is a collection
#  of keys values, used to store data values 
# like a map, which, unlike other data types 
# which hold only a single value as an element.

# In some languages it is known as map or
#  assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items

# mixed dictionary

# d2 = {(1,2,3):1,'hello':'world'}
# print(d2)

# # 2d dictionary -> Json
# s = {
#     'name':'nitish',
#     'college':'bit',
#     'sem':4,
#     'subjects':{
#         'dsa':50,
#         'math':67,
#         'english':70
#     }
# }
# print(s)

# using sequneve and dict function

# d4 = dict([('name','nitish'),('age',32)])
# print(d4,type(d4))

# d5 = {'name':'nitish','name':'rahul'}
# print(d5)
# duplicate keys arent allowed

# mutable items as keys are not allowed
# d6 = {'name':'nitish',[1,2,3]:2}
# print(d6)


# accessing items

# my_dict = {'name':'jack','age':20}
# # print(my_dict[0])#not allowed
# print(my_dict['name'])#enetr key to get value

# #get
# print(my_dict.get('age'))

# adding key value pair

# d4 = dict([('name','nitish'),('age',32),(3,3)])
# # print(d4)
# # # so if we want to add new key value  pair

# d4['gender']='male'
# d4['weight']=54
# print(d4)

# how to remove key value pair

# del


d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 54}
# pop
# d.pop(3)
# print(d)

# # popitem removes last item
# d.popitem()
# print(d)

# del
# del d['name']
# print(d)

# clear removes all
# d.clear()
# print(d)


# 2d

# s = {
#     'name':'nitish',
#     'college':'bit',
#     'sem':4,
#     'subjects':{
#         'dsa':50,
#         'math':67,
#         'english':70
#     }
# }
# print(s['subjects']['math'])

# s['subjects']['history']=78
# print(s)

# # to delete a specific subject

# del s['subjects']['math']
# print(s)

# # Editing key value pair

# s['sem'] = 5
# print(s)
# s['subjects']['dsa'] = 80
# print(s)

# Dictionary Operations

# memebrship(works on keys)
# iteration

# s = {
#     'name':'nitish',
#     'college':'bit',
#     'sem':4,
#     'subjects':{
#         'dsa':50,
#         'math':67,
#         'english':70
#     }
# }
# print('name' in s)

# d= {'name':'nitish','gender':'male','age':33}
# for i in d:
#     print(i)
# by doing this the key will print not values

d= {'name':'nitish','gender':'male','age':33}
for i in d:
    print(i,d[i])
    # this will print  keys and values 


# functions


# print(len(d))   

# print(sorted(d))

# print(min(d))

# print(max(d))

# items/keys/value

# print(d.items())
# tuple me key and value ko display karta

# print(d.keys())
# keys in tuple
# print(d.values())
# values in tuple

# update

# d1 = {1:2,3:4,4:6}
# d2 = {4:7,6:8}

# d1.update(d2)
# print(d1)


# dictionary comprehension

# {key:value for vars in iterable}

# print 1st 10 numbers and their squares

# d = {i:i**2 for i in range(1,11)}
# print(d)

# using existing dictionary

# comvert km in miles
# distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
# d ={key:value*0.63 for (key , value) in distances.items() }
# print(d)

# using zip

# days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

# d ={i:j for i,j in zip(days,temp_C)}
# print(d)

# using if condition

# display stock greater than 0
# products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
# d = {i:j for i,j in products.items() if j > 0 }
# print(d)

# Nested comprehension

# print tables from 2 to 4

# d = {i:{j:i*j for j in range(1,11)}for i in range(2,5)}
# print(d)
