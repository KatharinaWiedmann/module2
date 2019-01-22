# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 05:33:44 2018

@author: Katharina
"""

x = "There are {} types of people.".format(10)
binary = "binary"
do_not = "don't"
y = "Those who know {} and thoes whow {}.".format(binary, do_not)

print (x)
print (y)

print ("I said {}.".format(x))
print ("I also said: '{}'.".format(y))

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print (w+e)