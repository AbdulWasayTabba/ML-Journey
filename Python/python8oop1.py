# oop

# in python every thing is a 
# object e.g all data types

# what is oop
# the main power of oop is 
# that oop gives a programer the power
# to create his own data types

# today we will learn about 
# the principal called class

# L = [1,2,3]
# print(type(L))
# <class 'list'>

# L is a object of the class
# List 

# class is a blueprint
# keh us class ka object
# behave kese kare ga

# e.g list me 
# functions dale
# append,del,clear,extend etc

# class 
# me data or property (color ,model etc)
# and functions or behaviour(0 to 60 ?(a action))

# syntax tp create a object

# objectname = classname()

# L = list()

# s = str()

# object literal 
# L = [1,2,3]

# Pascal Case

# HelloWorld


# atm machine code

# class Atm:
#     # constructor
#     # is a function inside a class
#     # but constructor is a special fucntion
#     # because the constructor dosent have to be 
#     # called to be executed
#     # when you call the obj the constructor
#     # will automatically be called
#     def __init__(self):
#         self.pin = ''
#         self.balance = 0
#         self.menu()

#     def menu(self):
#         user_input = input("""Hi how can i help you?
#             1. Press 1 to create pin
#             2. Press 2 to change pin
#             3. Press 3 to check balance
#             4. Press 4 to withdraw
#             5. Anything else to exit""")
#         if user_input == '1':
#             self.create_pin()
#         elif user_input == '2':
#             self.change_pin()
#         elif user_input == '3':
#             self.check_balance()
#         elif user_input == '4':
#             self.withdraw()
#         else:
#             exit()
    
#     def create_pin(self):
#         user_pin = input('enter you pin')
#         self.pin = user_pin 

#         user_balance =int(input('enter balance'))
#         self.balance = user_balance

#         print('pin created succesfully')
#         self.menu()

#     def change_pin(self):
#         old_pin = input('enter old pin')
#         if old_pin == self.pin:
#             new_pin = input('enter new pin')
#             self.pin = new_pin
#             print('pin chnaged succesfully')
#             self.menu()

#         else:
#             print('wrong pin')
#             self.menu()
#     def check_balance(self):
#         user_pin =input('enter your pin')
#         if user_pin == self.pin:
#             print('your balance is : ',self.balance)
#             self.menu()
#         else:
#             print('wrong pin ')
#             self.menu()
#     def withdraw(self):
#         user_pin =input('enter your pin')
#         if user_pin == self.pin:
#             withdraw_amnt = int(input('enter amount'))
#             if withdraw_amnt <= self.balance:
#                 self.balance = self.balance-withdraw_amnt
#                 print('withdrawl succesful')
#                 print('balance left : ',self.balance)
#             else:
#                 print('insufficient funds')
        
#         else:
#             print('wrong pin')
#         self.menu()


# # to execute a class make a obejct of the 
# # class
# a = Atm()
# print(type(a))

# class diagram
# you can represent a class
# using a diagram 

# Methods vs function

# class ke andar wale 
# functions ko method bolte
# and jo class ke bahir hote
# unhe functions bolte


# e.g len() is a function
# and l.append() is a method
# because append is in the list 
# class

# Magic Methods(dunder methods)

# very important
# are special methods
# every magic mathod has a super power
# _ _name_ _ e.g constructor
# __init__
# super power of constructor is 
# that it gets called automatically
# when a object is made


# why is constructor beneficial

# woh cheeze ate jis ka control 
# ap user ko nahi dena chahte jese
# constructor is used to write
# configuration code


# self 

# self is a default parameter
# removes the restriction 
# that in oop only object can access
# evryhting nothing else
# so self removes that restriction

# self and the object points
# at the same memory address
# hence the self is the object

# self is nothing but the current
# object
# an object of the class inside the class
# for communication between methods



# we will create a data type 
# called fraction

# class Fraction:
#     # parametarised constructor
#     # a constructor which needs input
#     def __init__(self,x,y):
#         self.num = x
#         self.den = y

#     def __str__(self):
#         return '{}/{}'.format(self.num,self.den)

#     def __add__(self,other):
#         new_num = self.num*other.den+other.num * self.den
#         new_den = self.den*other.den

#         return '{}/{}'.format(new_num,new_den)
#     def __sub__(self,other):
#         new_num = self.num*other.den-other.num * self.den
#         new_den = self.den*other.den

#         return '{}/{}'.format(new_num,new_den)
    
#     def __mul__(self,other):
#         new_num = self.num*other.num
#         new_den = self.den*other.den

#         return '{}/{}'.format(new_num,new_den)
    
#     def __truediv__(self,other):
#         new_num = self.num*other.den
#         new_den = self.den*other.num

#         return '{}/{}'.format(new_num,new_den)
     
#     def convert_to_decimal(self):
#        return self.num/self.den
    

# fr1 = Fraction(3,4)
# fr2 = Fraction(1,2)
# print(type(fr1))
# print(fr1)#__str__
# # python will automatically go to 
# # the str fucnction that is the super power
# # of __str__

# print(fr1+fr2)#__add__
# print(fr1-fr2)#__sub__
# print(fr1*fr2)#__mul__
# print(fr1/fr2)#__truediv__

# print(fr1.convert_to_decimal())

