# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:05:23 2018

@author: Katharina
"""

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
    
if buses >  cars :
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print ("We still can't decide.")
    
buses += 20

if people > buses :
    print("Alright, let's just take the buses.")
else:
    print("Let's just stay at home then.")
    
if cars > people or buses > cars :
    print("This works.")