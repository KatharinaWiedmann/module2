# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:47:39 2018

@author: 612383447
"""
#
#OWN NOTES
#import random 

#import time
#
#def luckyNumberRandom():
#    name = input('Please type your name here: ')
#    print('Hello ' + name.upper())
#    number = int(input('Please give me a number: '))
#    
#    print ('Your lucky number is: ' +str(random.randint(1, number)))
#    
#
#
#startTime = time.time()
#
#print ('date and time', datetime.datetime.now())
#print ()
#print ('current time', datetime.datetime.now().time())
#
#luckyNumberRandom()
#
#processTime = time.time() - startTime
#
#print()
#print('programme running time: ', round(processTime,2),'second')  
#
#age = 15 
#isaTeen = age >= 13 and age <= 19
#
#print(isaTeen)
#

##task 3: IF
number = input("Choose a number between 1 and 10: ")
number = int(number)

if number > 10:
    print("Too high!") 
    
if number <= 0:
    print("Too low!")




##task 4.1: IF
number = input("Choose a number between 1 and 10: ")
number = int(number)

if number > 10:
   print("Too high!")

if 0 < number < 10: 
    print("Well done!")   
   
if number <= 0:
    print("Too low!")



##task 4.2: ELSE
number = input("Choose a number between 1 and 10: ")
number = int(number)

if number > 10:
   print("Too high!")
  
if number <= 0:
    print("Too low!")    
#must be an elif statement!
else:
    print("Well done!")   



 
##task 5: ELIF 
age = input("How old are you? ")
age = int(age)

if age < 13:
    print("child")
    
elif age < 18:
    print("teen")

elif age < 65:
    print("adult")
    
else: 
    print("pensioner")
    
##OWN NOTES 
#support = input("Which football club do you support? FC Bayern Munich or Dortmund? ")
#
#if (support == 'FC Bayern Munich'):
#    print("Well done, good choice!")
#else:
#    print ("Really, you support {} ?! WHYYYY?".format(support))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#







