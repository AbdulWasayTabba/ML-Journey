# Operators in Python
# Arithmetic Operators
# Relational Operators
# Logical Operators
# Bitwise Operators
# Assignment Operators
# Membership Operators


# # Arithmetric Operators
# print(5+6)

# print(5-6)

# print(5*6)

# print(5/2)

# print(5//2)#interger division

# print(5%2)#remainder

# print(5**2)#power


# Relational Operators

# print(4>5)

# print(4<5)

# print(4>=4)

# print(4<=4)

# print(4==4)

# print(4!=4)


# Logical Operators

# print(1 and 0)

# print(1 or 0)

# print(not 1)


# Bitwise Operators
# binary 

# bitwise and
# print(2 & 3)

#  bitwise or
# print(2 | 3)

#  bitwise xor
# print(2 ^ 3)

# print(~3)

# print(4 >> 2)
# leftshift 2 times

# print(5 << 2)
# right shift 2 times


# Assignment Operators

# = 
# a = 2

# a = 2

# a = a % 2
# a %= 2

# a++ ++a # this is not allowed


# print(a)

# Membership Operators
# yeh batata hai keh kiseme me yeh hai ya nahi
# in/not in

# print('D'  in 'Delhi') # = true
# print('D'  not in 'Delhi')# =false

# print(1 in [2,3,4,5,6])# =false

# Program - Find the sum of a 3 digit number 
# entered by the user

# d = int(input('enter a 3 digit number'))

# a = d%10
# d = d//10
# b = d%10
# d = d//10
# c=d%10
# result = a+b+c
# print(result)
  

# login program and indentation
# email -> wasay
# password -> 123

# email = input('enter email')
# password = input('enter password')
# if email == "wasay" and password =='123':
#     print('Welcome')
# elif email != "wasay" or password !='123':
#     print('try again')
#     email = input('enter email')
#     password = input('enter password')
#     if email == "wasay" and password =='123':
#        print('atlast welcome')
# else:
#     print('chordo')


# if-else examples
# 1. Find the min of 3 given numbers
# 2. Menu Driven Program

# a = int(input('enter a num'))
# b = int(input('enter a num'))
# c = int(input('enter a num'))
# if a<b and a<c:
#     print(a,"is the min number")
# elif b<a and b<c:
#     print(b,"is the min number")
# elif c<a and c<b:
#     print(c,"is the min number")

# or

# min of 3 number

# a = int(input('first num'))
# b = int(input('second num'))
# c = int(input('third num'))

# if a<b and a<c:
#   print('smallest is',a)
# elif b<c:
#   print('smallest is',b)
# else:
#   print('smallest is',c)


# menu driven calculator

# a = int(input("enter num"))
# b = int(input("enter num"))
# operator= input("enter operator")
# if operator == '+':
#     print(a+b)
# elif operator == '-':
#   print(  a-b)
# elif operator == '*':
#    print( a*b)
# elif operator == '/':
#    print( a/b)
# else:
#    print('wrong input')



#e.g of  menu driven 
# menu = input("""
# Hi! how can I help you.
# 1. Enter 1 for pin change
# 2. Enter 2 for balance check
# 3. Enter 3 for withdrawl
# 4. Enter 4 for exit
# """)

# if menu == '1':
#   print('pin change')
# elif menu == '2':
#   print('balance')
# else:
#   print('exit')


# Modules in Python
# math
# keywords
# random
# datetime

# jese library hote the c aur java me 

# math
# import math
# print(math.floor(6.8))

# keyword
# import keyword
# print(keyword.kwlist)
# random
# import random
# print(random.randint(1,100))

# datetime
# import datetime
# print(datetime.datetime.now())

# write help('modules')
# to find all the modules

# Loops in Python
# Need for loops
# While Loop
# For Loop

# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till 
# he/she enters a 0 and then find the avg

# number = int(input("enter a number"))
# i = 1
# while i <11:
#     print(number*i)
#     i+=1

# while loop with else
# x = 1
# while x<3:
#     print(x)
#     x+=1
# else:
#     print('limit crossed')

# guessing game

# generate a random number between 1 to 100
# import random as r
# jackpot = r.randint(1,100)
# a = int(input("enter number"))
# count = 1
# while a != jackpot:
    
#     if a < jackpot:
#         print("try a bit higher")
#     elif a>jackpot:
#         print("try a bit lower")
#     a = int(input("enter number"))
#     count+=1
# else:
#   print('congrats  :',count)



# For loop demo
# python ka for loop aik function
#  ko use karta hai
# range()
# 
# for i in range(1,11):
#   print(i) 
# for i in {1,2,3,4,5}:#list
#   print(i)

# for i in range(1,11,2):#interval
#   print(i) 
# for i in range(10,0,-1):#interval
#   print(i) 

# for i in 'Delhi':#string
#     print(i)

# aise yeh tuple,set ,dictinary,string,list pe bhi 
# iterate kar sakhta



# Program - The current population of a town is 10000. 
# The population of the town is increasing at the rate of 
# 10% per year. You have to write a program to find 
# out the population at
# the end of each of the last 10 years.

# pop = 10000
# for i in range(10,0,-1):
#     print('year ',i,' :',pop)
#     pop = pop/1.1


# Sequence sum

# 1/1!+2/2!+3/3!...
# import math 
# result =0
# n = int(input("enter num"))
# for i in range(1,n+1):
#     result = i/math.factorial(i)+result
# print(result)

# or 

# result =0
# fact=1
# n = int(input("enter num"))
# for i in range(1,n+1):
#     fact = fact*i
#     result =result + i/fact
# print(result)


    


