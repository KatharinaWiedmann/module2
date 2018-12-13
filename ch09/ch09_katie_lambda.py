# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:46:25 2018

@author: Katharina
"""

a = [ 50, 7, 9, 2, 22, 99, 72, 30, 90, 2 ]
b = (33, 56, 74, 2424, 93, 3, 8, 39)
my_favourite_fruits = ['ball', 'haus', 'banana']
x = ['ow', 'zs', 'hd', 'ab','cs']
z = ['ab', 'mk', 'gh', 'cs', 'uw']
y = sorted(x)

y[0] = 'zz'

x2 = [('j', 3, z),('f', 1, y),('q', 2, x)]

print(sorted(x2, key = lambda s: s[1]))
print()

print(sorted(x2, key = lambda s: s[2]))
print()

print(sorted(x2, key = lambda s: s[2][0][1]))
print()

print(sorted(x2, key = lambda s: s[2][3][1]))
print()

print(sorted(x2, key = lambda s: s[2][1][0]))
print()