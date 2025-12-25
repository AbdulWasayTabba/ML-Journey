# Q1:Count number of instances of
#  a class created in Python?
# Example: Say Car is any class.

# maruti = Car()
# bmw = Car()
# honda = Car()
# So after creating above instances. We want to count how many instances are created of Car class.

# For above example no of instances = 3.

# Write a program for above problem.


# class Car:
#     model = ''
#     year = ''
#     name = ''
#     __counter = 0

#     def __init__(self):
#         Car.__counter +=1

#     @staticmethod
#     def getcount():
#         return Car.__counter
    
# maruti = Car()
# bmw = Car()
# honda = Car()

# print(Car.getcount())


    

# Q-2: Create a deck of cards class.
#  Internally, the deck of cards 
#  should use another class, a card
#   class. Your requirements are:
# The Deck class should have a deal
#  method to deal a single card 
#  from the deck
# After a card is dealt, it is 
# removed
#  from the deck.
# There should be a shuffle
#  method which makes sure the deck 
#  of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit 
# (Hearts, Diamonds, Clubs, Spades)
#  and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# Deck Class
# It is class of all possible cards 
# in a deck. Total 52 cards.
# Methods - deal() it will take out 
# one card from the deck of cards.
# Deck of cards should get shuffeled
#  while creating the deck object.
# no of cards remaining in deck - 
# <number> should dsiplay on printing any deck object.
# Card class
# It is a class of card
# Atrributes - suit and value
# <suit> of <value> should dsiplay
#  on printing any card object.


# import random

# class Deck:
#     class Card:
#         def __init__(self, suit, value):
#             self.suit = suit
#             self.value = value

#         def __str__(self):
#             return f"{self.value} of {self.suit}"

#     def __init__(self):
#         self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#         self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#         self.cards = [Deck.Card(suit, value) for suit in self.suits for value in self.values]
#         self.shuffle()

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def deal(self):
#         if self.cards:
#             return self.cards.pop()
#         else:
#             return "No cards left to deal!"

#     def __str__(self):
#         return f"Number of cards remaining: {len(self.cards)}"

        

# deck = Deck()

# print(deck)             # Number of cards remaining: 52
# card = deck.deal()
# print(card)             # Example: Q of Clubs
# print(deck)        


# count number of instances of a class created in
# python

# class Car:
#     count = 0
#     def __init__(self,model,date):
#         self.model = model
#         self.date = date
#         Car.count += 1
#     def __str__(self):
#         return Car.count

# c = Car('g3',2020)
# print(c.__str__())


#  Create a deck of cards class.
#   Internally, the deck of cards
#   should use another class, a
#    card class. Your requirements are:


# import random
# class Deck:
#     class Card:
#         def __init__(self,value,suit):
#             self.value = value
#             self.suit = suit

#         def __str__(self):
#             return f"{self.value} of {self.suit}"
    
#     def __init__(self):
#         self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#         self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#         self.cards = [Deck.Card(suit, value) for suit in self.suits for value in self.values]
#         self.shuffle()
        
#     def shuffle(self):
#         random.shuffle(self.cards)
    
#     def deal(self):
#         if self.cards:
#             return self.cards.pop()
#         else:
#             return "No cards left to deal!"

    
#     def __str__(self):
#         return f"Number of cards remaining: {len(self.cards)}"



# Q-3: Find the area of a rectangle.
# Approach:

# The class name should be Rectangle.
# The constructor should accept two 
# parameters length 

# and height but you can't pass the
#  values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
# Create a method called area() which
#  has no parameters.
# Create a method called is_square()
#  which also has no 

# parameters. Return True if the
#  rectangle is a square otherwise return False.
# If you are using a if-else block 
# inside the is_square() 

# method, then use the one-linear syntax.

# class Rectangle:
#     def __init__(self,length,height):
#         self.length = length
#         self.height = height
    
#     def area(self):
#         a = self.length*self.height
#         return a
    
#     def is_square(self):
#         return True if self.length==self.height else False

# rec = Rectangle(10,10)
# print(rec.area())
# print(rec.is_square())    

        
            
# import datetime as dt

# class Product:
#     def __init__(self, mf_date, exp_date):
#         # Ensure the dates are datetime.date objects
#         self.mf_date = dt.datetime.strptime(mf_date, "%Y-%m-%d").date()
#         self.exp_date = dt.datetime.strptime(exp_date, "%Y-%m-%d").date()

#     def timeleft(self):
#         # Calculate the difference between expiry and manufacturing date
#         time_left = self.exp_date - self.mf_date
#         years = time_left.days // 365
#         months = (time_left.days % 365) // 30
#         days = (time_left.days % 365) % 30
#         return years, months, days

# # Create product with manufacturing and expiry dates in string format
# p = Product("2020-04-03", "2025-04-03")
# years, months, days = p.timeleft()
# print(f"Time left: {years} years, {months} months, {days} days")


# class Student:
#     def __init__(self, student_id, marks, age):
#         self.__student_id = student_id
#         self.__marks = marks
#         self.__age = age
       
#     def validate_marks(self):
#         if self.getmarks()>=0 and self.getmarks()<= 100:
#             return True
#     def validate_age(self):
#         if self.getage() >20:
#             return True
#     def check_qualification(self):
#         if self.validate_age() and self.validate_marks():
#             if self.getmarks()>=65:
#                 return True
#             else:
#                 return False
#         else:
#             return False
   
#     def student_id(self):
#         return self.__student_id


#     def getmarks(self):
#         return self.__marks

   
#     def setmarks(self, value):
#         self.__marks = value

  
#     def getage(self):
#         return self.__age


#     def setage(self, value):
#         self.__age = value

# s = Student(1234,65,23)
# print(s.check_qualification())


# class Scoop:
#     count = 0
#     __price = None
#     def __init__(self,flavor):
#         self.flavor=flavor
#         Scoop.count +=1

#     def sold(self):
#         print(Scoop.count)
    
#     def setprice(self,value):
#         self.__price = value   
#     def getprice(self):
#         return self.__price
# s1 = Scoop('mango')
# s1.setprice(20)
# print(s1.getprice())
# s2 = Scoop('banana')
# s2.setprice(30)
# print(s2.getprice())
# s3 = Scoop('stawberry')
# s3.setprice(40)
# print(s3.getprice())

# class Bowl:
#     count = 0
#     def __init__(self):
#         self.__scoop_list = []
#         Bowl.count+=1
#     def sold(self):
#         print(Bowl.count)

#     def add_scoops(self,*args:Scoop):
#         self.__scoop_list.extend(args)
    
#     def display(self):
#         total = 0
#         for i in range(0,len(self.__scoop_list)):
#            a = self.__scoop_list[i].flavor
#            b = self.__scoop_list[i].getprice()
#            total+=b
#            print('flavour : ',a,'| price : ',b )
#         print('total price : ',total)
# b1 = Bowl()
# b1.add_scoops(s1,s2,s3)
# b1.display()
# s1.sold()
# b1.sold()

            
            

