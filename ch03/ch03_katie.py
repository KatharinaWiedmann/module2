# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:44:13 2018

@author: 612383447
"""
#exercise 1
def hello_world_2args(b,y,p,a):
    print ("{} {} {} {}".format(b,y,p,a))
    
k = 'hello'
l = 'world'
m = 'love'
n = 'coding'
o = 'yo'
p = 'no'

hello_world_2args(k, l, o, p)
hello_world_2args(m, n, o, p)


#exercise 2 
def add_two_numbers (a, b, c):
    print ("Add {} plus {} is {}".format(a, b, c))
    
k = 3
y1 = 4
result = k + y1

thiswillnotshow = 5

add_two_numbers (k, y1, result)


#exercise 3
print (list(range(3,15)))

#exercise 4
def add_two_numbers_from_args (number1, number2):
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))
add_two_numbers_from_args(7,11)

#exercise 5
#this is for the computer/system 
def convert_distance_computer(miles):
    kilometers = (miles*8.0)/5.0
    return (miles, kilometers)


#this is for the user 
def convert_distance_user(miles):
    miles, kilometers = convert_distance_computer(miles)
    print ("Converting distance in miles to kilometers.")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    return (miles, kilometers)
    
#if variable just inside user function should be returned this is fine:
#convert_distance_user(9.0)
    
#if variable should be returned outside the function, do the next two lines:
miles = 10

miles, kilometers = convert_distance_user(miles)




#exercise 6 
#here the value will be saved and also printed 
def convert_temperature(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15 
    return ("That's {} in Fahrenheit and {} in Kelvin.".format(fahrenheit, kelvin))

convert_temperature(3)    

returned_value = convert_temperature(12)
print(returned_value)



    