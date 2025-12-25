# Problem 1: Combine two l
# ists index-wise(columns wise)

# list3 = []
# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
# for i,j in zip(list1,list2):
#     list3.append([i,j])
# print(list3)


# Problem 2: Add new item to list 
# after a specified item

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].insert(2,7000)

# print(list1)

# candy_list = ['Jelly Belly','Kit Kat',
#               'Double Bubble','Milky Way',
#               'Three Musketeers']
# no_of_items = [10,20,34,74,32]

# for i,j in zip(candy_list,no_of_items):
#     print(i,'-',j)


# Problem 4: Running Sum on list

# Output:

# [1,3,6,10,15,21]

# list1 = [1,2,3,4,5,6]
# list2 = []
# result = 0
# for i in range(0,len(list1)):
#     result +=list1[i]
#     list2.append(result)
        
# print(list2)

# Problem 5: You are given a list of integers. 
# You are asked to make a list by running 
# through elements of the list by 
# adding all elements greater and itself.

# i.e. Say given list is [2,4,6,10,1] 
# resultant list 
# will be [22,20,10,23].

# l1 = [2,4,6,10,1]
# l2 = []
# for i in range(0,len(l1)):
#     result = l1[i]
#     for j in range(0,len(l1)):
#         if l1[i]<l1[j] and i != j:
#             result += l1[j]
#     l2.append(result)
# print(l2)        



# Problem 6: Find list of common unique items 
# from two list. and show in increasing order


# Input

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:

# [34, 67, 89]

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# num3 =[]
# for i in num1:
#     for j in num2:
#         if i == j:
#             num3.append(j)
#             break
# print(sorted(num3))



# Problem 7: Sort a list of alphanumeric strings
# based on product value of numeric character in it.
# If in any string there
# is no numeric character take it's product value as 1.


# l1 = ['1ac21', '23fg', '456', '098d','1','kls']
# l2 = []

# result = 1
# for i in l1:
#     result = 1
#     for j in range(0,len(i)):
#         if ord(i[j]) >=48 and ord(i[j]) <=57:
#             result *= int(i[j])
        
#     l2.append((result,i))
# l2.sort(reverse=True)
# l3 = [item[1] for item in l2]
# print(l3)


# Problem 8: Split String of list on K character.

# l1 = ['CampusX is a channel', 'for data-science', 'aspirants.']
# l2 =[]
# for i in l1:
#     l2.extend(i.split(' '))
# print(l2)
    

# Problem 9: Convert Character
#  Matrix to single String using string comprehension.

# l1 = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'],
#   ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

# l2 =[''.join(i) for i in l1]


# result = ' '.join(l2)
# print(result)

# Problem 10: Add Space between Potential Words.
# Example:

# Input:

# ['campusxIs', 'bestFor', 'dataScientist']
# Output:

# ['campusx Is', 'best For', 'data Scientist']

# l1 = ['campusxIs', 'bestFor', 'dataScientist']
# l2 = []
# for i in l1:
#     result = ''
#     for j in range(0,len(i)):
#         if j>0 and i[j].isupper():
#             result +=' '+i[j]
#         else:
#             result += i[j]
#     l2.append(result)
# print(l2)


# Problem 11: Write a program that can 
# perform union operation on 2 lists
# Example:

# Input:

# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:

# [1,2,3,4,5,7,8]

# l1 =[1,2,3,4,5,1]
# l2 = [2,3,5,7,8]
# l3 = l1+l2
# l4 = []
# for i in l3 :
#     if i not in l4:
#         l4.append(i)
   
# print(l4)

   

# Problem 12: Write a program that can
# find the max number of each row of a matrix
# Example:

# Input:

# [[1,2,3],[4,5,6],[7,8,9]]

# l1 = [[1,2,3],[4,5,6],[7,8,9]]
# l2 =[]
# for i in l1:
#     l2.append(max(i))
# print(l2)
   


# Problem 13: Write a list comprehension 
# to print the following matrix
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# l1 = [[i for i in range(0,3)],[i for i in range(3,6)]
#       ,[i for i in range(7,10)]]
# print(l1)


# Problem 15: Write a list comprehension
# that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# l1 = [j for i in matrix for j in i ]
# print(l1)
