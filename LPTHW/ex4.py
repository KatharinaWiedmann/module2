# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:40:58 2018

@author: 612383447
"""
# assigns the value of 100 to the variable cars 
cars = 100 
#assigns the value of 4.0 to space_in_a_car
space_in_a_car = 4.0
#assigns value 30 to variable drivers
drivers = 30
#assigns value 90 to the variable passengers
passengers = 90
#assigns the two values of the value of cars subtracted by drivers to the new variable cars_not_driven 
cars_not_driven = cars - drivers
#assigns the value of the variable drivers to the variable cars_driven
cars_driven = drivers 
#assigns the value of cars_driven times space in car to the new variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#assigns the value of the variables passengers/cars_driven to the new variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven 

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")