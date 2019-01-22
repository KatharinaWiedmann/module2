# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 09:37:58 2018

@author: Katharina
"""

from shape import *
from pylab import random as r 
class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.dx = self.SpeedX()
        self.dy = self.SpeedY()
        
        def minmaxdefault(self, diameter):
            self.minx = diameter/2
            self.maxx = frame.width - (diameter/2)
            self.miny = diameter/2
            self.maxy = frame.height - (diameter/2)
        minmaxdefault(self,diameter)    
        
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        
    def goto(self, x, y): 
        self.figure.goto(x, y)
        
    def SpeedX(self):
        self.dx = 5 + 10* r()
        if r() > 0.5:
            self.dx = -self.dx
        else:
            self.dx = self.dx  
        return self.dx 
    
    def SpeedY(self):
        self.dy = 5 + 10* r()
        if r() > 0.5:
            self.dy = -self.dy
        else:
            self.dy = self.dy  
        return self.dy 
    
    def moveTick(self):   
        if self.x <= self.minx:
            self.dx = (self.dx)* -1
            
        if self.x >= self.maxx:
            self.dx = (self.dx)* -1
        
        if self.y <= self.miny:
            self.dy = (self.dy)* -1
        
        if self.y >= self.maxy:
            self.dy = (self.dy)* -1
            
        self.x = self.dx + self.x
        self.y = self.dy + self.y

           
        self.goto(self.x, self.y)
        

        

class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)

class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        def minmaxdefault(self, diameter):
            a1 = self.diameter**2 + self.diameter**2
            a2 = a1**0.5
            a3 = a2 / 2
            self.minx = a3
            self.maxx = frame.width - a3
            self.miny = a3
            self.maxy = frame.height - a3
        minmaxdefault(self,diameter)    

class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        

