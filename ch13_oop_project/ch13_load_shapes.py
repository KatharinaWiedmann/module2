# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:13:07 2018

@author: Katharina
"""

from shape import *

frame = Frame()
s1 = Shape('square', 100)
x = 0
y = 0
for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5
