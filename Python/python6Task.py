# While working with Python tuples, 
# we can have a problem in which we 
# need to perform concatenation of 
# records from the similarity of 
# initial element. This problem can 
# have applications in data domains 
# such as Data Science.

# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 

# test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# groups  = []#5,6  6,10
# seen_keys = []#5 6

# for i in test_list:
#     key = i[0]
#     value = i[1]
#     if key in seen_keys:
#         for j in groups:
#            if j[0]==key:
#              j.append(value)
    
#     else:
#         seen_keys.append(key)
#         groups.append([key,value])
# print(groups)


#Q2: Multiply Adjacent elements 
# (both side) and take sum of right and left 
# side multiplication result.
# For eg.

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) ->
#  (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)


# t = (1, 5, 7, 8, 10)
# l = []
# for i in range(0,len(t)):
#     if i == 0 and i <len(t)-1:
#         l.append(t[i] *t[i+1])
#     elif i >0 and i < len(t)-1:
#         l.append(t[i] *t[i+1]+t[i] *t[i-1])
#     elif i == len(t)-1:
#          l.append(t[i] *t[i-1])
#     else:
#         print('tuple isnt big enough')
# print(l)
# t1 = tuple(l)
# print(t1)


# Q3: Check is tuples are same or not?
# Two tuples would be same if
# both tuples have same element at same index

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# t1 and t2 are not same

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# for i,j in zip(t1,t2):
#     if i == j:
#         continue
#     else:
#         print('t1 and t2 are not the same')
#         break



# Q4: Count no of tuples, list 
# and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'}
#          ,('a', 'b'),['hi', 'bye'],['a', 'b']]

# Output:

# List-2
# Set-2
# Tuples-1

# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'}
#          ,('a', 'b'),['hi', 'bye'],['a', 'b']]
# List=0
# Set=0
# Tuples=0
# for i in list1:
#     if type(i) == list:
#         List +=1
#     elif type(i) == set:
#         Set +=1   
#     elif type(i) == tuple:
#         Tuples +=1    
# print('List-',List)
# print('Set-',Set)
# print('Tuples-',Tuples)


# Q5: Shortlist Students for a Job role
# Ask user to input students record and 
# store in tuples for each record. Then 
# Ask user to input three things he wants 
# in the candidate- Primary Skill, Higher 
# Education, Year of Graduation.

# Show every students record in form of tuples
# if matches all required criteria.

# It is assumed that there will be only one 
# primry skill.

# If no such candidate found, print No such
# candidate

# Input:

# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020

# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022
# Output
# ('Manohar', 'B.tech', 'Python', '2022')



# # Step 1: Input student records
# num = int(input('Enter number of records - '))
# student_records = []

# for i in range(num):
#     print(f'\nEnter details of student-{i+1}')
#     name = input('Enter Student name - ')
#     education = input('Enter Higher Education - ').lower()
#     skill = input('Enter Primary Skill - ').lower()
#     graduation = input('Enter Year of Graduation - ')
    
#     # Store each student as a tuple
#     student_records.append((name, education, skill, graduation))

# # Step 2: Input job role criteria
# print('\nEnter Job Role Requirement')
# required_education = input('Enter Higher Education - ').lower()
# required_skill = input('Enter Skill - ').lower()
# required_graduation = input('Enter Year of Graduation - ')

# criteria = (required_education, required_skill, required_graduation)

# # Step 3: Match and output
# matched = False
# for student in student_records:
#     if student[1:] == criteria:  # Compare education, skill, and graduation year
#         print(student)
#         matched = True

# if not matched:
#     print("No such candidate")




# Set


# Q1: Write a program to find set of common elements 
# in three lists using sets.
# Input : ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Output : [80, 20]


# ar1 = set([1, 5, 10, 20, 40, 80])
# ar2 = set([6, 7, 20, 80, 100])
# ar3 = set([3, 4, 15, 20, 30, 70, 80, 120])

# print(ar1&ar2&ar3)



# Q2: Write a program to count
# unique number of vowels using 
# sets in a given string. Lowercase
# and upercase vowels will be taken as different.
# Input:

# Str1 = "hands-on data science mentorship
#  progrAm with live classes at affordable 
# fee only on CampusX"
# Output:

# No of unique vowels-6

# s1 = {'a','e','i','o','u'}
# s2 = {'A','E','I','O','U'}
# t1 = set()
# Str1 = """hands-on data science mentorship
#  progrAm with live classes at affordable 
# fee only on CampusX"""

# count = 0
# for i in Str1:
#     if i in s1 or i in s2:
#         t1.add(i)
# print('No of unique vowels-',len(t1))



# Q3: Write a program to Check if
# a given string is binary string of or not.
# A string is said to be binary if 
# it's consists of only two unique characters.

# Take string input from user.

# Input: str = "01010101010"
# Output: Yes

# Input: str = "1222211"
# Output: Yes

# Input: str = "Campusx"
# Output: No

# str1 = input('enter string to see if binary')
# t1 = set()
# for i in str1:
#     t1.add(i)
# if len(t1) == 2:
#   print('true')
# else:
#     print('false')




# Q4: find union of n arrays.
# Example 1:

# Input:

# [[1, 2, 2, 4, 3, 6],
#  [5, 1, 3, 4],
#  [9, 5, 7, 1],
#  [2, 4, 1, 3]]
# Output:

# [1, 2, 3, 4, 5, 6, 7, 9]


# arr = [[1, 2, 2, 4, 3, 6],
#  [5, 1, 3, 4],
#  [9, 5, 7, 1],
#  [2, 4, 1, 3]]
# s = set()
# for i in arr:
#     for j in i:
#         s.add(j)
# print(s)
        


# Q5: Intersection of two lists.
# Intersection of two list means
# we need to take all those elements
# which are common to both of the 
# initial lists and store them into
# another list. Only use using 
# list-comprehension.
# Example 1:

# Input:

# lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
# lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
# Output:

# [9, 10, 4, 5]


# lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
# lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
# s1  = {i for i in lst1 if i in lst2 }
# print(list(s1))




# Dictionary
# Q1: Key with maximum unique values
# Given a dictionary with values
# list, extract key whose value
# has most unique values.

# Example 1:

# Input:

# test_dict = {"CampusX" : [5, 7, 9, 4, 0]
#              , "is" : [6, 7, 4, 3, 3]
#              , "Best" : [9, 9, 6, 5, 5]}
# Output:

# CampusX

# key = ''
# test_dict = {"CampusX" : [5, 7, 9, 4, 0],
#               "is" : [6, 7, 4, 3, 3],
#                 "Best" : [9, 9, 6, 5, 5]}
# maxuni = 0
# for i in test_dict:
#     unique = set(test_dict[i])
#     if len(unique)>maxuni:
#         maxuni = len(unique)
#         key = i
# print(key)
        
     


# Q2: Replace words from
# Dictionary. Given String,
# replace it’s words from lookup dictionary.
# Example 1:

# Input:

# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel"
#              , "DS" : "Data-Science"}
# Output:

# CampusX is the best channel 
# for Data-Science students.



# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel"
#              , "DS" : "Data-Science"}
# l = list(test_str.split(' '))

# for i in l:
#     if i in repl_dict:
#         print(repl_dict[i],end=' ')
#     else:
#         print(i,end=' ')




# Q3: Convert List to List of
# dictionaries. Given list values
# and keys list, convert these 
# values to key value pairs in 
# form of list of dictionaries.
# Example 1:

# Input:

# test_list = ["DataScience", 3, "is", 8]
# key_list = ["name", "id"]
# Output:

# [{'name': 'DataScience', 'id': 3}, 
#  {'name': 'is', 'id': 8}]



# test_list = ["DataScience", 3, "is", 8]
# key_list = ["name", "id"]

# for i in range(0,len(test_list),len(key_list)):
#     pair = test_list[i:i+2]
#     mapped = dict(zip(key_list,pair))
#     print(mapped)




# Q4: Convert a list of Tuples into Dictionary.
# Example 1:

# Input:
# [("akash", 10), ("gaurav", 12),
#   ("anand", 14), ("suraj", 20),
#     ("akhil", 25), ("ashish", 30)]

# output:

# {'akash': [10], 'gaurav': [12], 
#  'anand': [14], 'suraj': [20],
#    'akhil': [25], 'ashish': [30]}


# d = [("akash", 10), ("gaurav", 12),
#   ("anand", 14), ("suraj", 20),
#     ("akhil", 25), ("ashish", 30)]
# l1 = []
# l2 = []
# for i in d:
#     l1.append(i[0])
#     l2.append([i[1]])

# mapped = dict(zip(l1,l2))
# print(mapped)


        


# Q5: Sort Dictionary key and values List.
# Example 1:

# Input:

# {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# Output:

# {'a': [4, 19], 'b': [10, 12], 'c': [3]}


# d ={'c': [3], 'b': [12, 10], 'a': [19, 4]}

# d1 = dict(sorted(d.items()))

# print(d1)
