# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 03:42:55 2018

@author: Katharina
"""
#x = range(1,10,2)
#for n in x:
#    print (n)

#def add_two_numbers(number1, number2):
#    answer = number1 + number2
#    print("{} plus {} is {}.".format(number1, number2, answer))
#    return answer
#returned_value = add_two_numbers(3,4)



#def add_two_numbers2():
#    number1 = 10
#    number2 = 2
#    answer = number1 + number2
#    print("{} plus {} is {}.".format(number1, number2, answer))
#    
#add_two_numbers2()
#
#print(list(range(1,10,2)))
##
#def convert_distance(miles):
#    print("Converting miles into kilometers.")
#    miles = int(input("How many miles?"))
#    kilometers = (miles* 8.0)/5
#    print("Distance in kilometers:", kilometers)
#    return kilometers
#returned_value = convert_distance(0)
#    
#def temperature_converter(celsius):
#    print("This is a temperature converter.")
#    celsius = int(input("How many degrees is it in your country right now?"))
#    fahrenheit = celsius*9.0/5.0 +32
#    kelvin = celsius + 273.1
#    print("This is {} in Fahrenheit and {} in Kelvin".format(fahrenheit, kelvin))
#
#
#temperature_converter(0)


#def temp_con_2(celsius):
#    fahrenheit = celsius*9.0/5.0 +32
#    kelvin = celsius + 273.15
#    print("Fahrenheit", fahrenheit)
#    print("Kelvin", kelvin)
#
#temp_con_2(6)

#def add_two_numbers_and_a_return_value():
#    number1 = 1
#    number2 = 2
#    answer = number1 + number2
#    return answer 
#returned_value = add_two_numbers_and_a_return_value()
#print(returned_value)


#def is_even(i):
#    print("inside is_even")
#    return i%2 == 0
#
#returned_value = is_even(4)

#def is_even_with_return( i ):
#    print("With return")
#    remainder = i % 2
#    return remainder == 0
#
#is_even_with_return(3)
#
#print(is_even_with_return(3))
#
#
#def is_even_without_return( i ):
#    print("Without return")
#    remainder = i % 2
#    
#is_even_without_return(3)
#print(is_even_without_return(3))


number = int(input("Enter a number between 1-10: "))
if number < 0:
    print("Too low")
    
elif number > 10:
    print("Too high!")

else:
   print("{} will be your assigned number.".format(number))






















