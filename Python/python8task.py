# Q-1: Rectangle Class
# Write a Rectangle class in 
# Python language, allowing 
# you to build a rectangle with 
# length and width attributes.

# Create a Perimeter() method 
# to calculate the perimeter of 
# the rectangle and a Area() method 
# to calculate the area of ​​the rectangle.

# Create a method display() 
# that display the length, width, 
# perimeter and area of an object
#  created using an instantiation on rectangle class.

# class Rectangle:
#     def __init__(self,width,heigth):
#         self.width = width
#         self.height = heigth
        
#     def perimeter(self):
#         return 2*(self.width+self.height)
#     def area(self):
#         return self.width*self.height
    
#     def display(self):
#         print('lenght of rectangle is ',self.height)
#         print('width of rectangle is ',self.width)
#         print('perimeter of rectangle is ',self.perimeter())
#         print('area of rectangle is ',self.area())

# rec1 = Rectangle(3,4)
# rec1.display()




# Q-2: Bank Class
# Create a Python class called BankAccount
#  which represents a bank account, having
#  as attributes: accountNumber (numeric type),
#  name (name of the account owner as string type), balance.
# Create a constructor with 
# parameters: accountNumber, name, balance.
# Create a Deposit() method which
#  manages the deposit actions.
# Create a Withdrawal() method which
#  manages withdrawals actions.
# Create an bankFees() method to apply 
# the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display
#  account details. Give the complete code for the BankAccount class.
# Eg. After making above classes and methods, on executing below code:-

# newAccount = BankAccount(2178514584, "Mandy" , 2800)

# newAccount.Withdrawal(700)

# newAccount.Deposit(1000)

# newAccount.display()
# Output:

# Account Number :  2178514584
# Account Name :  Mandy
# Account Balance :  3100 ₹

# class BankAccount:
#     def __init__(self, accountNumber:int, name:str, balance:float):
#         self. accountNumber = accountNumber
#         self.name = name
#         self.balance = balance
#         self.menu()

#     def menu(self):
#         user_input = input("""Hi how can i help you?
#             1. Press 1 to deposit 
#             2. Press 2 to withdraw 
#             3. Press 3 to check balance
#             4. Anything else to exit""")
#         if user_input == '1':
#             self.deposit()
#         elif user_input == '2':
#             self.withdraw()
#         elif user_input == '3':
#             self.checkbalance()
        
#         else:
#             exit()
    
#     def deposit(self):
#         user_accnum = int(input('enter account number'))
#         if user_accnum == self.accountNumber:
#             dep_amnt = float(input('enter the amount you are deposting'))
#             self.balance += dep_amnt
#             print('deposit successfull')
#         self.menu()    

#     def withdraw(self):
#         user_accnum = int(input('enter account number'))
#         if user_accnum == self.accountNumber:
#             withdraw_amnt = float(input('enter the amount you are withdrawing'))
#             if withdraw_amnt >= self.balance:
#                 print('insufficent funds')
#             else :
#                 self.balance -= withdraw_amnt
#                 print('transaction successfull')
#         self.menu()  

#     def checkbalance(self):
#         user_accnum = int(input('enter account number'))
#         if user_accnum == self.accountNumber:
#             print('account balance is : ',self.balance)
#         self.menu()
             
# acc1 = BankAccount(1234,'wasay',10000)




# # Q-3:Computation class
# # Create a Computation class with a default constructor (without parameters) 
# # allowing to perform various calculations on integers numbers.

# # Create a method called Factorial() which allows to calculate 
# # the factorial of an integer n. Integer n as parameter for this method

# # Create a method called naturalSum() allowing to calculate 
# # the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

# # Create a method called testPrime() in the Calculation class
# #  to test the primality of a given integer n, n is Prime or Not?
# #  Integer n as parameter for this method.

# # Create a method called testPrims() allowing to test if two
# # numbers are prime between them. Two integers are prime to one another 
# # if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

# # Create a tableMult() method which creates and displays the
# # multiplication table of a given integer. Then create an 
# # allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

# # Create a static listDiv() method that gets all the 
# # divisors of a given integer on new list called Ldiv. 
# # Create another listDivPrim() method that gets all the prime divisors of a given integer.


# class Computation:
#     def __init__(self):
#         print('perform various calculations on integers')
#     def factorial(self,n:int):
#         result = 1
#         for i in range(1,n+1):
#             result *= i
#         print('factorial is : ',result)
#     def naturalsum(self,n:int):
#         result = 0
#         for i in range(1,n+1):
#              result += i
#         print('natural sum is : ',result)
    
#     def isPrime(self,n:int):
#         if n >1:
#             for i in range(2,n-1):
#                 if n%i == 0 :
#                     print('not a prime number')
#                     break
        
#             print(n, ' is a prime number')
    
#     def testPrims(self ,n:int,x:int):
#         l1,l2 = [],[]
#         if n > 1:
#             for i in range(2,n):
#                 if n%i == 0 :
#                     l1.append(i)
        
#         if x > 1:
#             for i in range(2,x):
#                 if x%i == 0 :
#                     l2.append(i)
        
#         if l1 in l2:
#             print(x," and ",n,' are not prime to each other')
#         else:
#             print(x," and ",n,' are  prime to each other')
    
#     def tableMult(self,n :int):
#         for i in range(1,11):
#             result = n*i
#             print(n," * ",i,' = ',result)
#     def allTableMult(self):
#         for i in range(1,11):
#             for j in range(1,11):
#                 result = i*j
#                 print(i," * ",j,' = ',result)
#             print()
#     def listDiv(self,n :int):
#         l1 = []
#         for i in range(1,n+1):
#             if n%i ==0:
#                 l1.append(i)
#         print(l1)

#     def listDivPrim(self,n:int):
#         l1 = []
#         prime = []
#         for i in range(1,n):
#             if n%i ==0:
#                 l1.append(i)
#         for i in l1:
#             if i < 2:
#               continue
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 prime.append(i)
#         print(prime)


# c = Computation()
# c.factorial(5)
# c.naturalsum(5)
# c.isPrime(7)
# c.testPrims(4,9)
# c.tableMult(9)
# c.allTableMult()
# c.listDiv(12)
# c.listDivPrim(12)






# Q-4: Build flashcard using class in Python.
# Build a flashcard using class in python. A flashcard 
# is a card having information on both sides, which can
# be used as an aid in memoization. Flashcards usually 
# have a question on one side and an answer on the other.

# Example 1:

# Approach:

# Create a class named FlashCard.
# Initialize dictionary fruits using init() method.
# Here you have to define fruit name as key and 
# it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
# Now randomly choose a pair from fruits by using
# random module and store the key in variable fruit
# and value in variable color.
# Now prompt the user to answer the color of
# the randomly chosen fruit.
# If correct print correct else print wrong.
# Output:

# welcome to fruit quiz
# What is the color of Strawberries
# pink
# Correct answer
# Enter 0, if you want to play again: 0
# What is the color of watermelon
# green
# Correct answer
# Enter 0, if you want to play again: 1



# import random 

# class FlashCard:
#     def __init__(self):
#         self.fruits = {"Banana": "yellow", "Strawberries": "pink"}

#     def guess(self):
        
#         fruit = random.choice(list(self.fruits.keys()))
#         color = self.fruits[fruit] 
#         color = color.lower()
#         user_inp = input(f'enter the color of the fruit :{fruit}')
#         if user_inp == color:
#             print('Correct answer')
#         else:
#             print('incorrect answer')
#         a = int(input('enter  0, if you want to play again: 1 to exit'))
#         if a == 0:
#             self.guess()
#         else:
#             exit()    



# f1 = FlashCard()
# f1.guess()








# Q-5: Problem 5 based on OOP Python.
# TechWorld, a technology training center, 
# wants to allocate courses for instructors.
# An instructor is identified by name, technology
# skills, experience and average feedback. An 
# instructor is allocated a course, if he/she
# satisfies the below two conditions:

# eligibility criteria:
# if experience is more than 3 years,
#  average feedback should be 4.5 or more
# if experience is 3 years or less, 
# average feedback should be 4 or more
# he/she should posses the technology 
# skill for the course
# Identify the class name and attributes 
# to represent instructors. Write a Python
# program to implement the class chosen with its attributes and methods.

# Note:

# Consider all instance variables to be private and methods to be public.
# An instructor may have multiple technology skills,
#  so consider instance variable, technology_skill to be a list.
# check_eligibility(): Return true if eligibility
#  criteria is satisfied by the instructor. Else, return false
# allocate_course(technology): Return true if the 
# course which requires the given technology can be allocated 
# to the instructor. Else, return false.
# Represent a few objects of the class, initialize 
# instance variables using setter methods, invoke
# appropriate methods and test your program.



# class TechWorld:
#     def __init__(self,experience,feedback,name,technology_skill:str):
#         self.__experience = experience
#         self.__feedback = feedback
#         self.__name = name
#         self.__technology_skill = technology_skill

#     def check_eligibility(self):
#         if self.__experience > 3 and self.__feedback>=4.5:
#             return True
#         elif self.__experience <= 3 and self.__feedback>=4:
#             return True
#         return False
    
#     def allocate_course(self,course : str):
#         if self.check_eligibility():
#             if self.__technology_skill.lower() == course.lower():
#                 print('congrats')
#                 return True
#             else:
#                 return False
#         else:
#             return False
# t1 = TechWorld(3,4,'abdul wasay tabba','data science')
# t1.allocate_course('data science')
     







        
    
    


        
                
    


    

        
        


