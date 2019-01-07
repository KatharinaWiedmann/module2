# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 09:54:02 2018

@author: Katharina
"""

from MovingShapes import *
frame = Frame()
shape1 = Square(frame, 100)
for i in range(100):
    shape1.moveTick()
