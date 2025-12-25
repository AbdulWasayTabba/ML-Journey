# Problem-1: Write a Python 
# function that takes a list 
# and returns a new list with
# unique elements of the first list.
# Exercise 1:

# Input:

# [1,2,3,3,3,3,4,5]
# Output:

# [1, 2, 3, 4, 5]

# def converter(L):
#     s = list(set(L))
#     return s
# l1 = [1,2,3,3,3,3,4,5]    
# print(converter(l1))



# Problem-2: Write a Python function
# that accepts a hyphen-separated 
# sequence of words as parameter and 
# returns the words in a hyphen-separated 
# sequence after sorting them alphabetically.
# Example 1:

# Input:

# green-red-yellow-black-white
# Output:

# black-green-red-white-yellow


# def sorterhyphen(x):
#     l1 = sorted([i for i in x.split('-')])
#     s1 = ''
#     count = 1
#     for i in l1:
#         s1+=i
#         if count<len(l1):
#            s1+='-'
#         count+=1
#     print(s1)
        

# s = 'green-red-yellow-black-white'
# sorterhyphen(s)

# or 

# def sorterhyphen(x):
#     sorted_list = sorted(x.split('-'))       # Split and sort
#     result = '-'.join(sorted_list)           # Join with hyphens
#     print(result)

# s = 'green-red-yellow-black-white'
# sorterhyphen(s)



# Problem 3: Write a Python function
# that accepts a string and calculate
#  the number of upper case letters 
# and lower case letters.
# Sample String : 'CampusX is an Online'
# ' Mentorship Program fOr EnginEering studentS.'
# Expected Output :
# No. of Upper case characters :  9
# No. of Lower case Characters :  47


# def counter(x):
#     lower = 0
#     upper = 0
#     for i in x:
#        if i.islower():
#            lower +=1
#        elif i.isupper():
#            upper +=1
#     print('No. of Upper case characters : ',upper)
#     print('No. of Lower case characters : ',lower)   
           

# s ='CampusX is an Online ' \
# 'Mentorship Program fOr EnginEering studentS.'
# counter(s)


# Problem 4: Write a Python program to
# print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# def lsteven(L):
#     L2 = []
#     for i in L:
#         if i %2 ==0:
#             L2.append(i)
#     print(L2)

# L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lsteven(L1)


# Problem 5: Write a Python function
# to check whether a number is perfect or not.
# A Perfect number is a number that
# is half the sum of all of its positive 
# divisors (including itself).

# Example :

# The first perfect number is 6, 
# because 1, 2, and 3 are its
# proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is 
# equal to half the sum of all 
# its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

# The next perfect number 
# is 28 = 1 + 2 + 4 + 7 + 14. This is 
# followed by the perfect numbers 496 and 8128.

# def isperfect(x):
#     t1 = 0
#     t2 = 0
#     pd = False
#     hpd = False
#     for i in range(1,x+1):
#         if x % i == 0 and i != x:
#             t1 += i
#             if t1 == x :
#                 pd = True
#         if x % i == 0:
#             t2 += i
#             if (t2/2) == x:
#                 hpd = True
#     if hpd and pd:
#         print(x,': Number is a perfect')
#     else:
#         print(x,': Number is not a perfect')
   

# a = int(input('enter a number to see if' \
# ' perfect or not'))
# isperfect(6)


# Problem-6: Write a Python function to 
# concatenate any no of dictionaries
# to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# def joindict(*args):

#     l= {}
#     for i in args:
#         l.update(i)
#     print(l)
   
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# joindict(dic1,dic2,dic3)



# Problem-7 Write a python function
# that accepts a string as input and 
# returns the word with most occurence.

# Input:
# hello how are you i am fine thank you
# Output
# you -> 2

# def occ(x:str):
#     l = x.split(' ')
#     t = 0
#     word = ''
#     for i in l :   
#         if l.count(i) > t:
#             t = l.count(i)
#             word = i
#     print( word,'-> ',t)        


# a = 'hello how are you i am fine thank you'
# occ(a)



# Problem-8 Write a python
# function that receives a 
# list of integers and prints 
# out a histogram of bin size 10

# Input:
# [13,42,15,37,22,39,41,50]
# Output:
# {11-20:2,21-30:1,31-40:2,41-50:3}

# def his(l1):
#     d = {}
#     for i in l1:
#         start = (i-1)//10*10 +1
#         end = start+9
#         keys = f"{start}-{end}"
#         if keys in d:
#             d[keys] += 1
#         else:
#             d[keys] = 1 
#     print(d)



# l = [13,42,15,37,22,39,41,50]
# his(l)    





# Problem-9 Write a python function
# that accepts a list of 2D co-ordinates
# and a query point, and then finds the 
# the co-ordinate which is closest in 
# terms of distance from the query point.

# List of Coordinates
# [(1,1),(2,2),(3,3),(4,4)]
# Query Point
# (0,0)
# Output
# Nearest to (0,0) is (1,1)


# def distance_coordinate(l,t):
#     import math
#     mindis = float('inf')
#     for i in l:
#         dist =math.sqrt((i[0]-t[0])**2 + (i[1]-t[1])**2)
#         if dist <  mindis:
#             mindis = dist
#             t1 = i
#     print('Nearest to ',t,' is ',t1)
         
        

# co =  [(1,1),(2,2),(3,3),(4,4)]
# qp = (0,0)
# distance_coordinate(co,qp)


# Problem-10:Write a python program that
# receives a list of strings 
# and performs bag of word operation 
# on those strings




# def bow(x:list):#bag of words
#     dic = {}
#     b = {}
#     for i in x:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i] = 1
#     b.update(dic)
#     return b


# s = ["John","likes","to","watch","movies","Mary","likes","movies","too"]
# print(bow(s))





# Problem 11: Write a Python
# program to
# add three given lists using
# Python map and lambda.

# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = [7,8,9,0]
# x =list(map(lambda *args:args,l1,l2,l3))
# print(x)

# # now if add 
# b = list(map(lambda x,y,z:x+y+z ,l1,l2,l3))
# print(b)



# Problem-12:Write a Python program 
# to create a list containing the
# power of said number in bases 
# raised to the corresponding
# number in the index using Python map.
# Input:

# list1 = [1,2,3,4,5,6]
# Output:

# [1,2,9,64,625,-]

# list1 = [9,4,5,3,2]

# x = [list1[0]**0]+list(map(lambda x:list1[x]**list1[x-1],range(1,len(list1))))
# print(list1)
# print(x)


# Problem-13 Using filter() and list() functions 
# and .lower() method filter all the vowels 
# in a given string.


# s = 'hello my name is abdul wasay tabba'
# vowels = list(filter(lambda x:x.islower() and x in 'aeiou'  ,s))
# print(vowels)


# Problem-14: Use reduce to convert a 2D list to 1D

# x = [
#     [1,2,3,4],
#     [5,6,7,8]
# ]
# import functools as ft
# a = ft.reduce(lambda b,y :b+y , x)
# print(a)




# Problem 15- A dictionary contains 
# following information about 5 employees:

# First name
# Last name
# Age
# Grade(Skilled,Semi-skilled,Highly skilled)
# Write a program using map/filter/reduce to a 
# list of employees(first name + last name) 
# who are highly skilled


# employees = [
#     {
#         'fname':'Nitish',
#         'lname':'Singh',
#         'age' : 33,
#         'grade':'skilled'
#     },
#     {
#         'fname':'Ankit',
#         'lname':'Verma',
#         'age' : 34,
#         'grade':'semi-skilled'
#     },
#     {
#         'fname':'Neha',
#         'lname':'Singh',
#         'age' : 35,
#         'grade':'highly-skilled'
#     },
#     {
#         'fname':'Anurag',
#         'lname':'Kumar',
#         'age' : 30,
#         'grade':'skilled'
#     },
#     {
#         'fname':'Abhinav',
#         'lname':'Sharma',
#         'age' : 37,
#         'grade':'highly-skilled'
#     }

# ]

# l1 =list( 
#     filter(None, 
#            map(lambda x :employees[x]['fname']+' '+employees[x]['lname'] if employees[x]['grade'] == 'highly-skilled'else None,range(0,len(employees)) )))
# print(l1)

# l2 = list(map(lambda x:x['fname'] + ' ' + x['lname'],list(filter(lambda x:True if x['grade'] == 'highly-skilled' else False,employees))))


