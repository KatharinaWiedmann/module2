# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:41 2018

@author: 612383447

"""
#USERINPUT TASK:
print('What is your name?')
name = input()
print('Hello {}!'.format(name))


from ch03_katie_function_file import *
#exercise 1
k = 'hello'
l = 'world'
m = 'love'
n = 'coding'
o = 'yo'
p = 'no'
hello_world_2args(k, l, o, p)
hello_world_2args(m, n, o, p)

#exercise 2
k = 3
y1 = 4
result = k + y1

thiswillnotshow = 5

add_two_numbers(k, y1, result)

#exercise 4
add_two_numbers_from_args(7,11)

#exercise 5
miles = 10
miles, kilometers = convert_distance_user(miles)

#exercise 6 
returned_value = convert_temperature(12)
print(returned_value)



