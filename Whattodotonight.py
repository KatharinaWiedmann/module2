# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:00:56 2018

@author: Katharina
"""

def WhatToDoTonight():
    choice = input('You got three different choices: A) Go to a restaurant in dalston? B)Go to South Acton or C) Meet up in the city centre.What do you choose? ')
    if choice == 'A':
        print('\nAlright, let\'s go to a restaurant in Dalston')
    elif choice == 'B':
        print('\nOkay, I will come to your house then..')
    elif choice == 'C':
        print('\nOkay, let\'s meet in the city centre.')
        
        
WhatToDoTonight()