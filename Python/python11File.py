# File handling

# Some Theory
# Types of data used for I/O:
# Text - '12345' as a sequence of unicode chars
# Binary - 12345 as a sequence of bytes of its binary equivalent
# Hence there are 2 file types to deal with
# Text files - All program files are text files
# Binary Files - Images,music,video,exe files

# How File I/O is done in most programming languages
# Open a file
# Read/Write data
# Close the file

# case 1 - if the file is not present

# f = open('sample.txt','w')
# # open to make a file name sample.txt and w for write
# f.write('Hello world')
# # write funtion
# f.close()
# to close the file after this you cant write 

# write multiple lines of string

# f = open('sample1.txt','w')
# f.write('hello world')
# f.write('\n how are you?')
# f.close()

# case 2 - if the file is already present e.g sample.txt

# f  = open('sample.txt','w')
# f.write('salam khan')
# this will replace the old content 
# so if you try to write in a existing file by doign this 
# it will replace the old content 


# how exactly open() works?
# file is basically a simple file
# jo hard drive me hai
# so when you write the open code
# python picks up the fiile and loads it in ram
# woh usse aik buffer memeory me load 
# karta hai 
# buffer memory me file character by character read
# hota hai
# and when you close it 
# file gets out of memory and goes to hard drive


# Problem with w mode
# introducing append mode
# f = open('sample1.txt','a')# a os for append
# # so it wont replace old content 
# f.write('\nI am fine')
# f.close()


# write lines
# agar bohot sare lines likhne hai aik sath

# List1 = ['\nhello','\nhi','\nare','\nyou','\nI','\nam','\nfine']
# f = open('sample.txt','a')
# f.writelines(List1)
# f.close()

# why do we close files
# beasue file gets loaded in ram toh if we dont do f.close 
# it will stay there and take up space
# and anyone on the computer will be able to access it 
# or get hacked so safety is also a reason

# reading lines from files
# -> using read

# read reads the whole content in one go
# read line read one line at a time

# f = open('sample.txt','r')#r = read
# s = f.read()#this will read all the content in the file
# print(s)
# s = f.readline()
# print(s)#this will print only the first line in the file
# f.close()

# you can also do f.read(10)
# so only 10 characters will be read

# f = open('sample.txt','r')
# print(f.readline(),end = '')#1st line
# print(f.readline())#2nd line
# f.close()

# reading entrie content using readline

# f = open('sample.txt','r')
# while True:
#     data = f.readline()
#     if data == '':
#         break
#     else:
#         print(data,end='')
# f.close()



# Using Context Manager (With)
# It's a good idea to
#  close a file after usage as it will free up the resources
# If we dont close it,
#  garbage collector would close it
# with keyword closes 
# the file as soon as the usage is over

# basically a replacemtn of f.close()

# with open('sample1.txt','w') as f:
#     f.write('selmaon bhai')

# try f.read() now

# with open('sample1.txt','r') as f:
#     print(f.read())

# with open('sample.txt','r')as f:
#     print(f.readline)


# moving within a file -> 10 char then 10 char
# with open('sample.txt','r') as f:
#   print(f.read(10))
#   print(f.read(10))
#   print(f.read(10))
#   print(f.read(10))
# this wont print the same thing 
# beacuse of buffer memory

# using this you can load large files 
# you can load it in chunks

# benefit? -> to load a big file in memory

# big_L = ['hello world' for i in range(1000)]
# with open('big.txt','w') as f:
#     f.writelines(big_L)

# with open('big.txt', 'r') as f:
#     chunk_size = 100
#     chunk = f.read(chunk_size)   # first read

#     while chunk:                 # now safe to check
#         print(chunk, end='')
#         chunk = f.read(chunk_size)  # read next chunk



# seek and tell function

# tell tells you where the buffer is 
# it tell you where you are

# seek is like defining a starting point  
# from where to start reading or printing

# with open('sample.txt','r') as f:
#   f.seek(15)
#   print(f.read(10))
#   print(f.tell())
  
#   print(f.read(10))
#   print(f.tell())


# seek during write
# with open('sample.txt','w') as f:
#   f.write('Hello')
#   f.seek(0)
#   f.write('Xa')
#   output will be Xallo so 
# because seek se the cursor goes to 0 and 
# overwrites 


# Problems with working in 
# text mode
# can't work with binary 
# files like images
# not good for other data 
# types like int/float/list/tuples


# working with binary file

# with open('screenshot1.png','r') as f:
#   f.read()
  #this will lead to a error
#   UnicodeDecodeError: 'utf-8' codec can't 
# decode byte 0x89 in position 0: invalid start byt


# working with binary file
# with open('screenshot1.png','rb') as f:
#   #rb is read binary
#   with open('screenshot_copy.png','wb') as wf:
#     # wb is write binary
#     wf.write(f.read())


# working with other data types
# with open('sample.txt','w') as f:
#   f.write(5)
#   will result in error beacuse unicode is needed
# hence

# working with other data types
# with open('sample.txt','w+') as f:   # w+ means write+read
#     f.write('5')
#     f.seek(0)                # move pointer back to start
#     print(int(f.read()) + 5) # prints 10

# more complex data types
# d = {
#     'name':'nitish',
#      'age':33,
#      'gender':'male'
# }

# with open('sample.txt','w+') as f:
#   f.write(str(d))
#   f.seek(0)
#   print(f.read())



# Serialization and Deserialization

# Serialization - process of converting 
# python data types to JSON format

# JSON = JAVASCRIPT ON NOTATION

# Deserialization - process of converting
# JSON to python data types

# Serialization using json module

# list
# import json
# L = [1,2,3,4]
# with open('demo.json','w')as f:
#     json.dump(L,f)
    # dump = me kya dump karna hai aur file ka object


# dictionary 

# d = {
#     'name':'nitish',
#      'age':33,
#      'gender':'male'
# }
# with open('demo.json','w')as f:
#     json.dump(d,f,indent=4)
    # indent for formating adding space


# deserialization

# import json

# with open('demo.json','r')as f:
#     d = json.load(f)
#     print(d)
#     print(type(d))


# serialize and deserialize tuple

# import json
# t = (1,2,3,4,5)
# with open('demo.json','w')as f:
#     json.dump(t,f)
# this shows that when you
# dump a tuple it turn into a list
# in the json file
# so when you deserialize it it will turn it
# into a list


# serialize and deserialize a nested dict

# import json
# d = {
#     'student':'nitish',
#      'marks':[23,14,34,45,56]
# }

# with open('demo.json','w') as f:
#   json.dump(d,f)



# Serializing and Deserializing custom objects

class Person:

  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender

person = Person('abdul','wasay',21,'male')

# import json

# # this is the way
# def show_object(person):
#   if isinstance(person,Person):
#     return  "{} {} age -> {} gender -> {}" \
#     "".format(person.fname,person.lname,person.age,person.gender)
# with open('demo.json','w')as f:

#   json.dump(person,f)
# ^
# this isnt possible 
# this is 
    # json.dump(person,f,default=show_object)
# default tell keh kese print karana hai
# and in show object method
# isinstance checks that 
# person is of Person class



# As a dict
# import json

# def show_object(person):
#   if isinstance(person,Person):
#     return {'name':person.fname + ' ' + 
#             person.lname,'age':person.age,'gender':person.gender}

# with open('demo.json','w') as f:
#   json.dump(person,f,default=show_object,indent=4)


# deserialize
# import json

# with open('demo.json','r')as f:
#   d = json.load(f)
#   print(d)
#   print(type(d))


# Pickling
# Pickling is the process whereby
# a Python object hierarchy is 
# converted into a byte stream,
# and unpickling is the inverse operation,
# whereby a byte stream
# (from a binary file or bytes-like object)
# is converted back into an object hierarchy.

# basically turning any object to bytes
# means it will be transfarable
# to another file
# and then you can deserialize it and use it


# class Person:

#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   def display_info(self):
#     print('Hi my name is',self.name,'and I am ',self.age,'years old')

# p = Person('nitish',33)

# import pickle
# with open('person.pkl','wb')as f:
#   #write binary
#   pickle.dump(p,f)

#   after the file is made you save it and make 
# another file over there you
# import pickle

# with open('person.pkl','rb')as f:
#   p = pickle.load(f)

# pickle load

# import pickle
# with open('person.pkl','rb')as f:
#   p = pickle.load(f)
#   print(p)


# Pickle Vs Json
# Pickle lets the user to store 
# data in binary format. JSON lets 
# the user store data in a
#  human-readable text format.

# for object you use pickle

# TASK--------------------------------

# Q-1: Write a function get_final_line(filename), 
# which takes filename as input and return final line of the file.

# with open('filet.txt','w')as f:
#   f.write('hi\n')
#   f.write('how\n')
#   f.write('are\n')
#   f.write('you\n')
#   f.write('???')

# def lastLine(fn):
#     with open(fn, 'r') as f:
#         last = ''
#         for line in f:     # iterate line by line
#             if line.strip() != '':
#                 last = line    # keep updating last
#         return last
# print(lastLine('filet.txt'))  
  

# Q-2: Read through a text file,
# line by line. Use a dict to keep
# track of how many times each vowel (a, e, i, o, and u) 
# appears in the file. Print the
# resulting tabulation -- dictionary.


# d = {'a':0,'o':0,'i':0,'e':0,'u':0}

# with open('filet.txt','r')as f:
#   for line in f:
#     for char in line:
#       if char in d:
#         d[char]+=1

# print(d)



# Q-3: Create a text file 
# (using an editor, not 
#  necessarily Python) containing
# two tab separated columns, with 
# each column containing a number.
# Then use Python to read through 
# the file you’ve created. For each
# line, multiply each first number
# by the second and include it in 
# the file in third column.
# In last add a line Total, by summing 
# the value of third column


# with open("C:\\Users\\HP\\Downloads\\prac.txt",'r')as f:
#    l = []
#    while True:
#      a = f.readline()
#      if a.strip() == '':
#        break
#      x =a.strip().split()
#      if x[0].isdigit() and x[1].isdigit():
#         l.append(x)
# print(l)

# sum = 0
# with open("C:\\Users\\HP\\Downloads\\prac.txt",'w')as f1:
#   result = 0
#   for i in l:
#     result = int(i[0])*int(i[1])
#     sum+=result
#     f1.write(i[0] + '\t' + i[1] + '\t' + str(result) + '\n')

# with open("C:\\Users\\HP\\Downloads\\prac.txt",'a')as f2:
#   f2.write('Total   '+str(sum))


# with open('file1.txt','w')as f:
#     f.write('abc def\n')
#     f.write('ghi jkl\n')
  

# def reverse(file1,file2):
#   with open(file1, 'r') as f, open(file2, 'w') as f2:
#     temp = f.readline()
#     while temp:      
#       f2.write(temp.strip()[::-1]+'\n')
#       temp = f.readline()
        

# reverse('file1.txt','file2.txt')




# Q-5: Create a Serialized dict 
# of frequency of words in the file. 
# And from given list of words,
#  using serialized dict show word count.

# strings = """Alice was beginning to get very tired of sitting by her sister
#             on the bank, and of having nothing to do:  once or twice she had
#             peeped into the book her sister was reading, but it had no
#             pictures or conversations in it, `and what is the use of a book,'
#             thought Alice `without pictures or conversation?'

#             So she was considering in her own mind (as well as she could,
#             for the hot day made her feel very sleepy and stupid), whether
#             the pleasure of making a daisy-chain would be worth the trouble
#             of getting up and picking the daisies, when suddenly a White
#             Rabbit with pink eyes ran close by her.

#             There was nothing so VERY remarkable in that; nor did Alice
#             think it so VERY much out of the way to hear the Rabbit say to
#             itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
#             it over afterwards, it occurred to her that she ought to have
#             wondered at this, but at the time it all seemed quite natural);
#             but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
#             POCKET, and looked at it, and then hurried on, Alice started to
#             her feet, for it flashed across her mind that she had never
#             before seen a rabbit with either a waistcoat-pocket, or a watch to
#             take out of it, and burning with curiosity, she ran across the
#             field after it, and fortunately was just in time to see it pop
#             down a large rabbit-hole under the hedge."""
# import string
# word_list = ['alice', 'wonder', 'natural']
# data = {word:0 for word in word_list}
# import json
# with open('cs.json','w')as f:
#   json.dump(data,f,indent=4)
# with open('cs.json','r')as f2:
#   d = json.load(f2)
#   l = strings.split()
#   for word in l:
#     clean_word = word.lower().strip(string.punctuation)
#     if clean_word in d:
#       d[clean_word]+=1
#   print(d)
# with open('cs.json','w')as f3:
#   json.dump(d,f3)


# Q-6: Given a string calculate length of the string using recursion.
# s = "abcd"

# def length(s):
#   if s == '':
#     return 0
#   else:
#     return 1 + length(s[1:])
# print(length(s))
    


# Q-7: Write a function that 
# accepts two numbers and 
# returns their greatest common
# divisior. Without using any loop    


# gcd(16,24) will give 8

# def gcd(a, b):
#     if b == 0:       # base case
#         return a
#     else:
#         return gcd(b, a % b)  # recursive call



    

class Solution(object):
    def isValid(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
           return True
        x = s.split()
        l = []
        for idx,i in enumerate(x):
           if i == '[' or i == '(' or i == '{':
              l.append(i)
           elif i == ']':
              if '[' in l:
                 continue
              else:
                 return False
           elif i == '}':
              if '{' in l:
                 continue
              else:
                 return False 
           elif i == ')':
              if '(' in l:
                 continue
              else:
                 return False
        return True
              
           
           
        
               
           

o = Solution()
s = "(]"
print(o.isValid(s))

        
           
           
              


