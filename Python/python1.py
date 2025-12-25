# python is case sensitive

# print("Hello World")
# print(7.7)
# print(True)
# print('Hello',1,4,5,True)

# print('Hello',1,4,5,True,sep='/')
# sep is for seprator by default it is ' '

# print('hello')
# print('world')
# this will casue hello and world to be in diffrent lines
# to change it

# print('hello',end='-')
# print('world')
# this causes hello world to be in
#  same line with - joining them


# complex

# print(5+6j)

# list

# print([1,2,3,4,5])

# tuple

# print((1,2,3,4,5))

# sets

# print({1,2,3,4,5})

# Dictionary

# print({'name':'Abdul','gender':'Male'})

# type

# print(type([1,2,3]))

# variable

# container for future use
# name = 'abdul'
# print(name)
# a=5
# b=6
# print(a+b)

# dynamic typing
# a = 5 
# where you do not tell the data type of the variable

# static typing
# int a = 5

# Dynamic Binding 
# a=5
# print(a)
# a='abdul'
# print(a)
# yeh code chale ga because 
# a aik fixed data type nahi hai
# hence dynaic not static

# stylish way yo create variable
# a,b,c = 1,2,3
# print(a,b,c)

# another way
# a=b=c=5
# print(a,b,c)

# keyword & identifiers

# keywords
# bus main wale keyword ko variable ke tarah nahi use karna
# like print aur while aur etc

# identifiers

# koi bhi name dete ho woh hota hai 
# jese koi funtion
# variable
# class
# rules hote hai
# jese you cant start with a number

# typeconversion
# implicit vs explicit
# e.g print(5+6.7)
# the result will come in float 
# so python will automatically convert the data type 
# but this always dosent work
# e.g print(4+'4')
# this isnt possible because int + str
# yeh python nahi krta khude toh
# explicit type conversion karna parhta hai
# e.g int('4') = 4
#  str(5) ='5'
# float(4) = 4.0

# static vs dynamic
# static is when user only takes information not input
# dynamic is when user interacts by giving input

# input

# name = input("Enter your name: ") 
# print("Hello,", name)

# email = input("enter email")
# print(email)

# fnum = int(input("enter first number"))
# snum = int(input('enter second number'))
# print(fnum,snum)
# result = fnum+snum
# print(result)
# print(type(fnum))#=int

# or

# fnum = input("enter first number")
# snum = input('enter second number')
# print(fnum,snum)
# result = int(fnum)+int(snum)
# print(result)
# print(type(fnum)) #=str


# Literals
# jo bhi raw value ko store kar rahe ho woh liberal hai
# e.g a = 2 
# 2 is literal and a is variable


# a = 0b1010 #Binary Literals
# b = 100 #Decimal Literal 
# c = 0o310 #Octal Literal
# d = 0x12c #Hexadecimal Literal

# #Float Literal
# float_1 = 10.5 
# float_2 = 1.5e2 # 1.5 * 10^2
# float_3 = 1.5e-3 # 1.5 * 10^-3

# #Complex Literal 
# x = 3.14j

# print(a, b, c, d)
# print(float_1, float_2,float_3)
# print(x, x.imag, x.real)


# # binary
# x = 3.14j
# print(x.imag)



# string = 'This is Python'
# strings = "This is Python"
# char = "C"
# multiline_str = """This is a multiline string with more than one line code."""
# unicode = u"\U0001f600\U0001F606\U0001F923"
# raw_str = r"raw \n string"

# print(string)
# print(strings)
# print(char)
# print(multiline_str)
# print(unicode)
# print(raw_str)

# a = True + 4
# b = False + 10

# print("a:", a)#true = 1
# print("b:", b)#false =0


# k = None/variable declaration
# a = 5
# b = 6
# print('Program exe')