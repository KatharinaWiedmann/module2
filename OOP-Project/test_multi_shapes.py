# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:58:52 2019

@author: Katharina
"""

from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = []
for i in range(numshapes):
    shapes.append(Square(frame,100))
for i in range(100):
    for shape in shapes:
        shape.moveTick()