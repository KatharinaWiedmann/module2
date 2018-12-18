# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:57:50 2018

@author: Katharina
"""

from random import randint
def rollingdices():    
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    secretnumber = dice1 + dice2
    print(secretnumber)
    return secretnumber
 

    
def guessing():
    guess = ' '
    while guess != 'quit':
        secretnumber = rollingdices() 
        even = ((secretnumber) % 2 == 0)
        odd = ((secretnumber)% 2 != 0)
        guess = input('Do you think it\'s even or odd?')
        if guess == 'even' and even is True:
            print('Well done! The secretnumber is {}.'.format(secretnumber))
        elif guess == 'even' and odd is True:
            print('Sorry the secretnumber is {} and is therefore odd.'.format(secretnumber))
        elif guess == 'odd' and odd is True:
            print('Well done! The secretnumber is {}.'.format(secretnumber)) 
        elif guess == 'odd' and even is True:
            print('Sorry the secretnumber is {} and is therefore even.'.format(secretnumber)) 
 
    print('Thanks for playing - bye!')
guessing()

     