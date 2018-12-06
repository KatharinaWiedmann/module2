# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:13:05 2018

@author: Katharina
"""
#
#print ("You enter a dark room with two doors. Where do you go?Left or right")
#door = input()
#
#if door == 'left' :
#    print ("Well done, you will survive!")
#    
#elif door == 'right':
#    print("Oh, oh, you should have gone to the other side.")
#    
##else:
##    print("Wait, where do you want to go? You can only go left or right.")


print("You enter a dark room with two doors. Do you go through door#1 or door #2?")
      
door = input()

if door == "1":
    print("There's a giant bear in here eating a cheese cake. What do you do?")
    print('1. Take the cake')
    print('2. Scream at the bear.')
    
    bear = input()
    
    if bear == '1':
        print('The bear eats your face off. Good job.')
    elif bear == '2':
        print('The bear eats your legs off.Good job.')
    else:
        print("Well, doing {} is probably better. Bear runs away.".format(bear))
        
elif door == '2':
    print("You really wanted to scream at the bear?")
    print("Let's see if that was clever. You now need to decide what's your favourite number between 1-10")
    
    number = input()
    
    if number == '1' or number == '2' or number == '3':
        print("Well done. The bear is scared of the number {}.".format(number))
        print("He walks away.")
    else:
        print("You just lost that game. The bear hates the number {} and he will eat you now.".format(number))
        
else:
    print("You stumble around and fall on a knife.")