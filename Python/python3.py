# Nested loop
# Example unique pairs 

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)

# pattern
# *
# **
# ***
# rows =int(input("enter number of rows"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()        

# 1
# 121
# 12321
# 12343221
# rows = int(input('enter rows'))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     for k in range(i-1,0,-1):   
#         print(k,end='')
#     print()        

# loop control statement

# break
# control
# pass
# continue:skips current iteration

# for i in range(1,10):
#     if i ==5:
#         break
#     print(i)



# e.g prime number only

# lower = int(input('enter'))
# upper = int(input('enter'))

# for i in range(lower,upper+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         print(i)

# continue

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

# pass:bus ignore kar
#  deta hai error se bachne ke liye 

# for i in range(1,10):
#     pass

# Strings 

# s='hello'
# s="hello"
# # multiline strings triple inverted comma
# s='''hello'''
# s-str('hello')
# print(s)

# indexing

# s = 'hello world'
# python will internally assign index position
# to evry single character this is 
# positive indexing
# print(s[0])for h

# negative indexing 

# s = 'hello world'
# right se left
# print(s[-1])#last character d
# print(s[-7])#for o


# slicing

# substring nikalne ke liye

# s = 'hello world'
# print(s[:5]) # for hello
# print(s[2:])#for 2 wale index baad sare llo world
# print(s[0:6:2])#hlo every 2 index till 6 from 0
# print(s[6:0:-1])#start from 6 and go back becaue of 
# # -1
# print(s[6:0:-2])#ulta jao ge but 
# # skip karte jao ge aik index ko due to -2
# print(s[::-1])#used to reverse the string

# negative indexing in slicing

# s = 'hello world'

# print(s[-5:])#for world

# ab world ko ulta oprint karna hai

# print(s[-1:-6:-1])


# editing and deleting Strings

# s ='hello world'
# s[0]='H'
# not possibkle beacuse
# python strings are immutable
# cant be changed

# s='hello world'
# del s techinaclly delete karta
# but not in memory
# print(s)

# Operations on Strings

# Arthemetic operations(+,*)
# print('delhi'+' '+'mumbai')

# print('delhi'*5)
# print("*"*50)

# Relational operations

# sare kam karte hai

# print('delhi' == 'mumbai')

# print('mumbai'> 'pune')
# leciographivally

# print('Pune'>'pune')
# P ke ascii value is lesser than p

# print('hello' and 'world')#prints world
# print('hello' or 'world')#prints hello
# print('' and 'world')

# print(not '' ) # = true
# python empty string ko false consder karta

# for i in 'hello':
#     print(i)
# loop use ho sakhte strings pe

# print('D' in 'Delhi')
# print('D' not in 'Delhi')

# Common Functions
# jo sabhi data types pe chalte hai

# print(len('hello world'))

# max 
# print(max('hello world'))
# min 
# ascii se calculate kare gam in strings
# print(min('hello world'))

# sorted 
# print(sorted('hello world'))
# print(sorted('hello world',reverse = True))
# descing order ke liye reverse

# Capitalize
# s = 'hello world'
# print(s.capitalize())
# covverts the first character of the string
# into capital 

# Title
# s = 'hello world'
# print(s.title())
# converts all the words first letter to capital

# upper
# s = 'hello world'
# print(s.upper())
# all to capital

# lower
# s = 'hello world'
# print(s.lower())
#  all to lower

# swap case
# s = 'hello world'
# print(s.swapcase())
# opposite me convert in terms of case



# count

# s = 'hello world'

# print(s.count('l'))
# counts number of times l came in string

# find

# print(s.find('ll'))
# finds index

# index
# print(s.index('ll'))

# endswith

# print(s.endswith('d'))

# startswith

# print(s.startswith('h'))

# format

# name = 'nitish'
# gender = 'male'

# print('hi my name is' \
# ' {} and i am a {}'.format(name,gender))
# variable string me dalne ke liye 
# order matters

# print('hi my name is' \
# ' {1} and i am a {0}'.format(gender,name))
# you can define the order

# yeh sare functions string ke orignal value 
# ko change nahi karta
# python aik new string banata hai 
# aur phir display karta 
# hence string is immutable

# isalnum:check karta keh string alpha numeric hai ya nahi
# isalpha :check karta keh string all alphabets hai ya nahi
# isdigit: check karta keh string me digits hai ya nahi
# isidentifier:variable which are valid wale true aye ge 

# * split
# given sentence ko word by word break kar deta

# s= 'hi my name is nitish'
# print(s.split())
# print(s.split('is'))

# join
# reverse of split where you join sentences

# print(' '.join(['hi', 'my', 'name', 'is', 'nitish']))

# replace

# s = 'hi my name is nitish'
# print(s.replace('nitish','campus x'))

# * Strip
# removes trailling spaces

# print('nitish           '.strip())
# removes spaces

# task

# Find the length of a given string without using the len() function
# count = 0
# s = input('enter your name')
# for i in s:
#     count +=1
# print(count)    
        

# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh


# s = input('enter your email')
# pin = s.find('@')
# print(s[:pin])


# Count the frequency of a particular character
#  in a provided string. 
# Eg 'hello how are you' is the string, the 
# frequency of h in this string is 2.

# s = input("enter a word")
# f = input("enter the letter pf which you would like " \
# "to find the frequency of")

# print(s.count(f))


# Write a program which can remove a particular 
# character from a string.

# s = input('enter')
# d = input('enter a character you want to remove')
# result = ''
# for i in range(0,len(s)):
#     if s[i] != d:
#         result +=s[i]
# print(result)




# Write a program that can check whether 
# a given string is palindrome or not.
# abba
# malayalam


# a=''
# b=''
# s = input('enter')
# if len(s)%2 == 0:
#     for i in range(0,int(len(s)/2)):
#         a=a+s[i]
#     for j in range(int(len(s)/2),len(s)):
#         b=b+s[j]
#     if a == b[::-1]:
#         print('palindrome true') 
#     else:
#         print('Not a palindrome')       
 
# else:

#     for i in range(0, len(s) // 2):
#         a += s[i]
#     for j in range(len(s) // 2 + 1, len(s)):
#         b += s[j]
# if a == b[::-1]:
#     print('Palindrome true')
# else:
#     print('Not a palindrome')        
    



# Write a program to count
#  the number of words in a string without split()

# s = input("enter")
# temp = ''
# count=0
# L = []
# for i in s:
#     if i == ' ':
    
#         count +=1
#         L.append(temp)
#         temp = ''
#     else:
#         temp = temp+i

# print(L)
# print(count)    


# Write a python program to
#  convert a string to title case without using the title()

# s = input('enter')
# result = ''
# for i in range(len(s)):
#         if i == 0 and 'a' <= s[i] <= 'z':  
#             result += chr(ord(s[i]) - 32)
#         elif s[i - 1] == ' ' and 'a' <= s[i] <= 'z':
#             result += chr(ord(s[i]) - 32)
#         else:
#             result += s[i] 

# print(result)     


# or

# s = input('enter the string')

# L = []
# for i in s.split():#hi how are you
#   L.append(i[0].upper() + i[1:].lower())

# print(" ".join(L))



# Write a program that can convert an integer to string.

# i = int(input('enter number '))

# i = str(i)
# print(i,type(i))


# number = int(input('enter the number'))

# digits = '0123456789'
# result = ''
# while number != 0:
#   result = digits[number % 10] + result
#   number = number//10

# print(result)
# print(type(result))






    
