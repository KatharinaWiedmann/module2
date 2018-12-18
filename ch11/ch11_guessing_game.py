# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:09:25 2018

@author: Katharina
"""

from random import randint
def guess(attempts, range):
    number = randint(1, range)
    counter = 0
    player_guess = 1
    guesses_left = 1
    print("Welcome! Can you guess my secret number? You have {} guesses." .format(attempts))
    print('secret number', number)
    while player_guess != number and guesses_left > 0:
        player_guess = int(input('Type your guess here: '))
        counter += 1
        guesses_left = attempts - counter
        if player_guess > number:
            print('Too high')
            print('You have {} guesses left'.format(guesses_left)) 
        elif player_guess < number: 
            print('Too low')
            print('You have {} guesses left'.format(guesses_left)) 
        elif player_guess == number:
            print('Well done! You have guessed correctly and you will eave the game now. Thanks for playing.')
            break
guess(6, 20)    
    
    
    
    
    
