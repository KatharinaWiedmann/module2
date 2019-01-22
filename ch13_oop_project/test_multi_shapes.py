# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:58:52 2019

@author: Katharina
"""

from MovingShapes import *
frame = Frame()
numshapes = 5
shapes = []
size = 60
for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
for i in range(300):
    for shape in shapes:
        shape.moveTick()
frame.close()