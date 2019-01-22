# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:04:41 2018

@author: Katharina
"""

class Vehicle(object):
    
    def __init__(self, colour, wheelcount):
        self.colour = colour
        self.wheelcount = wheelcount 
        
    def startEngine(self):
        print('Vrooooom')
        
    def stopEngine(self):
        print('STOOOOOOP')
        
def _changeGears():
    print('bad')
    
class Car(Vehicle):
    
    @staticmethod
    def driving():
        print('I can drive')
        
 
        
    def startEngine(self):
        print('I am broken')
        print(self.colour)
        print(self.wheelcount)

    def _changeGears(self):
        print('I changed gears')
        
#car1 = Car('blue', 4)    
Car.driving()
        
