# -*- coding: utf-8 -*-
"""

@author: Katharina
"""

class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom 
        return Fraction(top, bott)
    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num 
        bott = self.denom*other.denom 
        return Fraction(top, bott)
    def __float__(self):
        return self.num/self.denom 
    def inverse(self):
        return Fraction(self.denom, self.num)
        
a = Fraction(2, 4)
b = Fraction(8, 9)
c = a + b
print(a)
print(b)
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
