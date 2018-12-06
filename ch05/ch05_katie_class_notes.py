## -*- coding: utf-8 -*-
#"""
#Created on Wed Dec  5 10:13:12 2018
#
#@author: 612383447
#"""
##exercise 1 
##class Customer(object):
##    """A customer of ABC Bank with a checking account. Customers have the following properties:
##    Attributes:
##        name: A string representing the customer's name. 
##        balance: A float tracking the current balance of the customer's account.
##    """
##    
##    def __init__(self, name, balance, age):
##        """Return a Customer object whose name is *name* and starting balance is *balance*."""
##        self.name = name
##        self.balance = balance
##        self.age = age
##        
##    def withdraw(self, amount):
##        """Return the balance remaining after withdrawing *amount* dollars."""
##        if amount > self.balance:
##            raise RuntimeError('Amount greater than available balance.')
##        self.balance -= amount
##        return self.balance
##        
##    def deposit(self, amount):
##         """Return the balance remaining after depositing *amount* dollars."""
##         self.balance += amount
##         return self.balance
##     
##customer1 = Customer('Jason Taylor', 1000.0, 9)
##customer2 = Customer('Jonathan X', 8000.0, 7)
##
##NEXT WEEK: TRY WITH A LOOP!
#
##print(customer1.name)
##print("Starting balance:", customer1.balance)
##customer1.withdraw(400)
##print("New balance after withdrawing:", customer1.balance)
##print("Customer age:", customer1.age)
##
##print(customer2.name)
##print("Starting balance:", customer2.balance)
##customer2.deposit(600)
##print("New balance after depositing:", customer2.balance)
##print("Age of {}:".format(customer2.name), customer2.age)
#
#
#
#
#
###exercise 2
##class Animal():
###the following two will assign values to all animals     
##    def eat(self):
##        print('yum')
##        
##    def __init__(self, favourite_colour, balance, age):
##        self.favourite_colour = favourite_colour
##        self.balance = balance
##        self.age = age
###Dog inherits eating and init(with own values!) from animals         
##class Dog(Animal):
##    def bark(self):
##        print('Woof!')
###Cat inherits eating and init(with own values!) from animals         
##class Cat(Animal):
##    def meow(self):
##        print('Meow')
###Labrador inherits eating and init(with own values!) from animals and barking from Dog. Also it can sleep         
##class Labrador(Dog):
##    def sleep(self):
##        print("Let me sleep!")
###Main_Coon inherits eating and init(with own values!) from animals and meowing from cat. Also it can sleep.        
##class Main_Coon(Cat):
##    def sleep(self):
##        print("Let me sleep!")        
##        
##Snoopy = Dog('blue', 70, 8)
##Snoopy.bark()
##Snoopy.eat()
##print("Snoopy's favourite colour, balance and age:", Snoopy.favourite_colour,",", Snoopy.balance,",", Snoopy.age)
##
##Ella = Cat('red', 90, 7)
##Ella.eat()
##Ella.meow()
##print("Ella's favourite colour:", Ella.favourite_colour)
##
##Polly = Main_Coon('green', 800, 3)
##Polly.eat()
##Polly.meow()
##Polly.sleep()
##print("Polly's favourite colour, balance and age:", Polly.favourite_colour,",", Polly.balance,",", Polly.age)
#
#exercise 3:
#class family_member():
#
#    def __init__(self, name, age):
#            self.name = name
#            self.age = age    
#        
#    
#    def family_house(self, house_location, family_name):
#       print("Hi, so you are part of the {} family".format(family_name),"and you live in {}. ".format(house_location))   
#        
#
#class grandparent(family_member):
#    def teaching_values(self, value):
#        print("Oh, so you say {} is the most important. Good choice".format(value))
#        
#class parent(grandparent):
#  
#    def teaching_softskill(self, softskill):
#        print("The most important soft skill is: {}.".format(softskill), "You can pass this softskill onto your children.")
#
#class child(parent):
#    def applying_value_and_softskill(self, value, softskill):      
#        print("Your parents taught you: {}". format(value), "and {} " .format(softskill))
#        
##script has to be separate!   
# 
#Opa = grandparent('Franz', 80)       
#family_name = input("Hi. Please type your family name here: ")        
#
#house_location = input("Where do you live? ") 
#Opa.family_house(house_location, family_name) #needs to have the variables which should be 
#
#value = input("As a grandparent you can decide which is the most important value of the family. Please type it in here: ")
#Opa.teaching_values(value)
#    
#      
#Papa = parent('Andreas', 55)
#family_name = input("Hi. Please type your family name here: ")  
#house_location = input("Where do you live? ") 
#Papa.family_house(house_location, family_name)
#softskill = input("As a parent you can decide which is the soft skill the kids should learn. Please tell me what's most important: ")
#Papa.teaching_softskill(softskill)    
#
#
##CHECK THIS LATER
#Kind = child('Katie', 23)
#family_name = input("Hi. Please type your family name here: ")  
#house_location = input("Where do you live? ") 
#Kind.family_house(house_location, family_name)
#Kind.applying_value_and_softskill(value, softskill)    
#
#
#exercise 4:
class Animal():
    def eat(self):
        print("yum")
class Dog(Animal):
    def bark(self):
        print("woof!")
        
class Robot():
    def move(self):
            print("...move move move...")

class CleanRobot(Robot):
    def clean(self):
        print("I vacuum dust")
        
class SuperRobot():
    def __init__(self):
        #This class contains 3 objects - can do everything  
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
        self.o4 = Animal()
    
    def playGame(self):
        print("alphago game")
    def move(self):
        return self.o1.move() #using robot class method
    def bark(self):
        return self.o2.bark() #using dog class method
    def clean(self):
        return self.o3.clean() #using cleanrobot method 
    def eat(self):
        return self.o4.eat() #using animal method 
    
machineDog = SuperRobot()
machineDog.move()
machineDog.bark()
machineDog.clean()

#SupermachineDog can do everything, even eat! 
SupermachineDog = SuperRobot()
SupermachineDog.move()
SupermachineDog.bark()
SupermachineDog.clean()
SupermachineDog.eat()

    
































