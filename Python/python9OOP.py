# Write OOP classes to handle 
# the following scenarios:
# A user can create and view
#  2D coordinates
# A user can find out the 
# distance between 2 coordinates
# A user can find find the 
# distance of a coordinate from origin
# A user can check if a point 
# lies on a given line
# A user can find the distance
#  between a given 2D point and a given line



# class Point:#<x,y>
#     def __init__(self,x,y):
#         self.x_cod = x
#         self.y_cod = y
    
#     def __str__(self):
#         return '<{},{}>'.format(self.x_cod,self.y_cod)
    
#     def euclidean_distance(self,other):
#         import math
#         return math.sqrt((self.x_cod-other.x_cod)**2
#                           +(self.y_cod - other.y_cod)**2)
    
#     def distance_from_origin(self):
#         return self.euclidean_distance(Point(0,0))


# class Line:#AX+BY+C     
#     def __init__(self,A,B,C):
#         self.A = A
#         self.B = B
#         self.C = C

#     def __str__(self):
#         return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    
#     def point_on_line(self,point:Point):
#         if self.A * point.x_cod + self.B * point.y_cod + self.C == 0:
#             return 'lies on the line'
#         else:
#             return "does not lie on line"
    
#     def shortest_distance(self,point:Point):
#         return abs((self.A*point.x_cod+self.B*point.y_cod+self.C)/(self.A**2+self.B**2)**0.5)
        
# l1 = Line(3,4,5)
# l2 = Line(1,1,-2)
# p4 = Point(1,1)
# print(l1)

# p1 = Point(0,0)
# p2 = Point(1,1)
# p3 = Point(4,5)

# print(p1)

# #2
# print(p2.euclidean_distance(p3))
# print(p3.euclidean_distance(p2))

# #3
# print(p2.distance_from_origin())

# #4
# print(l1.point_on_line(p4))
# print(l2.point_on_line(p4))

# #5
# print(l1.shortest_distance(p4))
# print(l2.shortest_distance(p4))#lies on the line



# How objects access attributes



# class Person:

#   def __init__(self,name_input,country_input):
#     self.name = name_input
#     self.country = country_input

#   def greet(self):
#     if self.country == 'india':
#       print('Namaste',self.name)
#     else:
#       print('Hello',self.name)

# # how to access attributes

# p = Person('nitish','india')
# print(p.country)
# print(p.name)
# p.greet()

# what if i try to access non_existent attributes

# p.gender() 
# this will result in a error



# you can make a attribute outside of class

# p.gender = 'male' 
# print(p.gender)




# Reference Variables
# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to 
# an existing object does not create a new object



# object without a reference
# class Person:

#   def __init__(self):
#     self.name = 'nitish'
#     self.gender = 'male'

# p = Person()
# q = p

# # p is just a vairable name jis ke pass
# # memory address hai object ka 

# # q is also pointing to the same adress as p

# print(id(p))
# print(id(q))
# so if you change anything in one both 
# will change

# print(p.name)
# print(q.name)
# q.name = 'ankit'
# print(q.name)
# print(p.name)


# Pass by reference

# class Person:
#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# # outside the class hence it is a
# # function
# def greed(person: Person):
#   print('Hi my name is',person.name,' and i am' \
#   ' a',person.gender)
#   p = Person('abdul','male')
#   return p #function returning a object

# p1 = Person('nitish','male')
# x = greed(p1)
# print(x.name)
# print(x.gender)



# objects in python are mutable 
# just like list sets and dictionaries
# but you can make them imutable


# a isntance variable is the vairable in the constructor
# which value can be changed for diffrent obj
# p1 = Person('steve')
# p2 = Person('will')
# isntace variable is a special kind of object
# jisa value object ke opper depend karta hai



# encapsulation

# core fundemenatal of oop programming
# private attribute karna hota
# keh bahir se koi vairables access nahi kar 
# sake woh hide ho jata hai

# class Atm:

#   # constructor(special function)->superpower -> 
#   def __init__(self):
#     print(id(self))
#     self.pin = ''
#     self.__balance = 0#balance attribute is private
#     # because it has double underscore before
#     # its name
#     self.menu()

#   def get_balance(self):
#     return self.__balance

#   def set_balance(self,new_value):
#     if type(new_value) == int:
#       self.__balance = new_value
#     else:
#       print('beta bahot maarenge')

#   def __menu(self):
#     user_input = input("""
#     Hi how can I help you?
#     1. Press 1 to create pin
#     2. Press 2 to change pin
#     3. Press 3 to check balance
#     4. Press 4 to withdraw
#     5. Anything else to exit
#     """)

#     if user_input == '1':
#       self.create_pin()
#     elif user_input == '2':
#       self.change_pin()
#     elif user_input == '3':
#       self.check_balance()
#     elif user_input == '4':
#       self.withdraw()
#     else:
#       exit()

#   def create_pin(self):
#     user_pin = input('enter your pin')
#     self.pin = user_pin

#     user_balance = int(input('enter balance'))
#     self.__balance = user_balance

#     print('pin created successfully')

#   def change_pin(self):
#     old_pin = input('enter old pin')

#     if old_pin == self.pin:
#       # let him change the pin
#       new_pin = input('enter new pin')
#       self.pin = new_pin
#       print('pin change successful')
#     else:
#       print('nai karne de sakta re baba')

#   def check_balance(self):
#     user_pin = input('enter your pin')
#     if user_pin == self.pin:
#       print('your balance is ',self.__balance)
#     else:
#       print('chal nikal yahan se')

#   def withdraw(self):
#     user_pin = input('enter the pin')
#     if user_pin == self.pin:
#       # allow to withdraw
#       amount = int(input('enter the amount'))
#       if amount <= self.__balance:
#         self.__balance = self.__balance - amount
#         print('withdrawl successful.balance is',self.__balance)
#       else:
#         print('abe garib')
#     else:
#       print('sale chor')


# a story for encapsulation

# you are a senior programmer and are told to make 
# a atm class code in which you 
# make the attributes private but your junior 
# programmer hated you and decided to make some 
# chnages to the code from his end
# so he did _classname__attributename
# and changed then the code didnt work
# so the hr got called he got fired then 
# another junior came and said the code requires
# chnage in the program from my end so plz remove the private
# but due to contriversy you ddidnt want to make it public
# so you make getter and setter because these methods
# can access the private attributes adn show their value
# thats why i have made getbalance and setbalance
# this the logic behind getter and setter and this is 
# encapsulation



# collection of objects 

# list of objects
# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# p1 = Person('nitish','male')
# p2 = Person('Abdul','male')
# p3 = Person('Hira','female')

# l1 = [p1,p2,p3]
# s = {p1,p2,p3}
# t = (p1,p2,p3)
# for i in l1:
#   print(i.name,' ',i.gender)
# for i in s:
#   print(i.name,' ',i.gender)
# for i in t:
#   print(i.name,' ',i.gender)

#   # all possible

# d = {'p1':p1,'p2':p2,'p3':p3}

# for i in d:
#   print(d[i].gender)



# Static Variables



# class Atm:

#   __counter = 1#static variable

#   # constructor(special function)->superpower -> 
#   def __init__(self):
#     print(id(self))
#     self.pin = ''
#     self.__balance = 0
#     self.cid = Atm.__counter
#     Atm.__counter = Atm.__counter + 1
#     #self.menu()

#   # utility functions
#   @staticmethod
#   def get_counter():
#     return Atm.__counter


#   def get_balance(self):
#     return self.__balance

#   def set_balance(self,new_value):
#     if type(new_value) == int:
#       self.__balance = new_value
#     else:
#       print('beta bahot maarenge')

#   def __menu(self):
#     user_input = input("""
#     Hi how can I help you?
#     1. Press 1 to create pin
#     2. Press 2 to change pin
#     3. Press 3 to check balance
#     4. Press 4 to withdraw
#     5. Anything else to exit
#     """)

#     if user_input == '1':
#       self.create_pin()
#     elif user_input == '2':
#       self.change_pin()
#     elif user_input == '3':
#       self.check_balance()
#     elif user_input == '4':
#       self.withdraw()
#     else:
#       exit()

#   def create_pin(self):
#     user_pin = input('enter your pin')
#     self.pin = user_pin

#     user_balance = int(input('enter balance'))
#     self.__balance = user_balance

#     print('pin created successfully')

#   def change_pin(self):
#     old_pin = input('enter old pin')

#     if old_pin == self.pin:
#       # let him change the pin
#       new_pin = input('enter new pin')
#       self.pin = new_pin
#       print('pin change successful')
#     else:
#       print('nai karne de sakta re baba')

#   def check_balance(self):
#     user_pin = input('enter your pin')
#     if user_pin == self.pin:
#       print('your balance is ',self.__balance)
#     else:
#       print('chal nikal yahan se')

#   def withdraw(self):
#     user_pin = input('enter the pin')
#     if user_pin == self.pin:
#       # allow to withdraw
#       amount = int(input('enter the amount'))
#       if amount <= self.__balance:
#         self.__balance = self.__balance - amount
#         print('withdrawl successful.balance is',self.__balance)
#       else:
#         print('abe garib')
#     else:
#       print('sale chor')


# instance variuable = onject variable

# static vairbale = class variable

# agar manager ne bola
# keh har user ke id diff hone chaiye
# so you apply static variable
# because every user needs a diffrent id

# static varible ko class ke name ke sath
# use karte ho instead of self

# to access a static method you dont haver to 
# define a object you can use 
# class name then method name
# and above the method write 
# @staticmethod to identify
# which method is static


# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         l2 = list1 +list2
#         l3 = []
#         for i in range(0,len(l2)):
#             for j in range(0,len(l2)):
#                 if l2[i]<=l2[j] and l2[i] != l2[j]:
#                     l3.append(l2[i])
#                 else :
#                     continue
#         return l3


# l1 = [1,2,4]
# l2 = [1,3,4]
# s1 = Solution()
# print(s1.mergeTwoLists(l1,l2) )
