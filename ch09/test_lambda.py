# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:23:01 2018

@author: Katharina
"""

y = [22, 3, 7, 9, 11]
z = ['the', 'cat', 'sat', 'on', 'the', 'mat']
z[0] = 22
z[1] = 5
x = [22, 11, 3, 9, 2]

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
#print(x2)

print(sorted(x2, key=lambda s:s[2][0]))
