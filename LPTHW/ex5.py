# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = 'Katharina Wiedmann'
age = 23 #not a lie 
height = 174 #cm
weight = 63 #kg
eyes = "Blue"
teeth = "White"
hair = "Brown"

print (("Let's talk about {}").format(name))
print (("She is {} inches tall.").format (height/2.54))
print (("She is {} lbs heavy.").format(weight*2.205))
print ("Actually that's not too heavy.")
print (("She has got {} eyes and {} hair").format(eyes, hair))
print (("Her teeth are usually {} depending on the coffee.").format(teeth))

print (("If I add {}, {} and {} I get {}").format(age, height, weight, age + height + weight))