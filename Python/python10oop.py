# inheritance

# example
# class Customer:

#   def __init__(self,name,gender,address):
#     self.name = name
#     self.gender = gender
#     self.address = address

#   def print_address(self):
#     print(self.address._Address__city,self.address.pin,self.address.state)

#   def edit_profile(self,new_name,new_city,new_pin,new_state):
#     self.name = new_name
#     self.address.edit_address(new_city,new_pin,new_state)

# class Address:

#   def __init__(self,city,pin,state):
#       self.__city = city
#       self.pin = pin
#       self.state = state

#   def get_city(self):
#     return self.__city

#   def edit_address(self,new_city,new_pin,new_state):
#     self.__city = new_city
#     self.pin = new_pin
#     self.state = new_state

# add1 = Address('gurgaon',122011,'haryana')
# cust = Customer('nitish','male',add1)

# cust.print_address()

# cust.edit_profile('ankit','mumbai',111111,'maharastra')
# cust.print_address()
# method example
# what about private attribute


# Example

# parent
# class User:

#   def __init__(self):
#     self.name = 'nitish'
#     self.gender = 'male'

#   def login(self):
#     print('login')

# # child
# class Student(User):

#   def __init__(self):
#     self.rollno = 100

#   def enroll(self):
#     print('enroll into the course')

# u = User()
# s = Student()

# print(s.name)
# s.login()
# s.enroll()


# What gets inherited?
# Constructor
# Non Private Attributes
# Non Private Methods



# constructor example

# class Phone:#parent
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):#child
#     pass

# s=SmartPhone(20000, "Apple", 13)
# s.buy()


# constructor example 2

# child cant access private members of the class
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# getter
#     def __show(self):
#         print(self.__price)

# class SmartPhone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print ("Inside SmartPhone constructor")

# s=SmartPhone("Android", 2)
# s.__show#this will result in error because method is private
# s.brand


# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def show(self):
#         print("This is in child class")
        
# son=Child(100)
# print(son.get_num())
# son.show()
# getter will get private values


# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self,val,num):
#         self.__val=val

#     def get_val(self):
#         return self.__val
        
# son=Child(100,10)
# print("Parent: Num:",son.get_num())
# print("Child: Val:",son.get_val())

# error


# class A:
#     def __init__(self):
#         self.var1=100

#     def display1(self,var1):
#         print("class A :", self.var1)
# class B(A):
  
#     def display2(self,var1):
#         print("class B :", self.var1)

# obj=B()
# obj.display1(200)



# Method Overriding
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")

# s=SmartPhone(20000, "Apple", 13)

# s.buy()


# Super Keyword
# using super you can call parent stuff

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")
#         # syntax to call parent ka buy method
#         super().buy()

# s=SmartPhone(20000, "Apple", 13)

# s.buy()


# super -> constuctor
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         print('Inside smartphone constructor')
#         super().__init__(price, brand, camera)#parent constructor
#         self.os = os
#         self.ram = ram
#         print ("Inside smartphone constructor")

# s=SmartPhone(20000, "Samsung", 12, "Android", 2)

# print(s.os)
# print(s.brand)

# super is always used inside a class not outside 
# used in a child class
# super cannot access variables only methods



# can super access parent ka data?
# using super outside the class
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")
#         # syntax to call parent ka buy method
#         print(super().brand)

# s=SmartPhone(20000, "Apple", 13)

# s.buy()


# Inheritance in summary
# A class can inherit from another class.

# Inheritance improves code reuse

# Constructor, attributes, methods get
#  inherited to the child class

# The parent has no access to the
#  child class

# Private properties of parent are not
#  accessible directly in child class

# Child class can override the attributes 
# or methods. This is called method overriding

# super() is an inbuilt function which is
#  used to invoke the parent class methods and constructor


# class Parent:

#     def __init__(self,num):
#       self.__num=num

#     def get_num(self):
#       return self.__num

# class Child(Parent):
  
#     def __init__(self,num,val):
#       super().__init__(num)
#       self.__val=val

#     def get_val(self):
#       return self.__val
      
# son=Child(100,200)
# print(son.get_num())
# print(son.get_val())



# Types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Multiple Inheritance(Diamond Problem)
# Hybrid Inheritance


# single inheritance
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# SmartPhone(1000,"Apple","13px").buy()



# multilevel
# grandfather->father->child
# child will inherit from grandfather and father
# class Product:
#     def review(self):
#         print ("Product customer review")

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(20000, "Apple", 12)

# s.buy()
# s.review()


# Hierarchical
# one parent and multiple children

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# class FeaturePhone(Phone):
#     pass

# SmartPhone(1000,"Apple","13px").buy()
# FeaturePhone(10,"Lava","1px").buy()



# Multiple
# two parent and one child
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class Product:
#     def review(self):
#         print ("Customer review")

# class SmartPhone(Phone, Product):
#     pass

# s=SmartPhone(20000, "Apple", 12)

# s.buy()
# s.review()



# hybrid is also a inheritance type
# which onvloves joining the other types
# which invloves heiarchiel 
# multiple and single



# the diamond problem
# https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class Product:
#     def buy(self):
#         print ("Product buy method")

# # Method resolution order
# class SmartPhone(Phone,Product):
#     pass

# s=SmartPhone(20000, "Apple", 12)

# s.buy()


# Polymorphism
# Method Overriding
# Method Overloading
# Operator Overloading

# class Shape :
#    def area(self,radius):
#       return 3.14*radius*radius
#    def area(self,l,b):
#       return l*b
   
#    method overloading with the same name
#    but diffrent functionalities
#    depending on the input 
# in python this wont work 
# unlike java
# this will give a error

# this is method overloading in a smart way     #   
# class Shape:

#   def area(self,a,b=0):
#     if b == 0:
#       return 3.14*a*a
#     else:
#       return a*b

# s = Shape()

# print(s.area(2))
# print(s.area(3,4))


            
        
        
# Abstraction 

# abstract method jusme koi code nahi likha hua hota
# till now we made concrete methods

# basically ap details hide kar dete ho
# and as a senior programmer you can make sure
# that the child classes will do something you want
# like in this example it was neccessary to make the 
# security method in the Mobile Class

# from abc import ABC,abstractmethod 
# class BankApp(ABC):

#     def database(self):
#         print('connected to database')
    
#     @abstractmethod
#     def security(self):#abstract class
#         pass

# class MobileApp(BankApp):
#     def mobile_login(self):
#         print('login into mobile')
    
#     def security(self):#yeh zaroori tha
#         print('mobile security')

# ob = MobileApp()
# ob.security()

 
