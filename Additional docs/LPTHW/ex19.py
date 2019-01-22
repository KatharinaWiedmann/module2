# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:23:28 2018

@author: 612383447
"""
#
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print("You have {} cheeses!".format(cheese_count))
#    print("You have {} boxes of crackers!".format(boxes_of_crackers))
#    print("Man that's enough for a party!")
#    print("Get a blanket.\n")
#    
#print("We can just give the function numbers directly:")
#cheese_and_crackers(20,30)
#
#print ("Or we can use variables from our script:")
#amount_of_cheese = 10
#amount_of_crackers = 50
#
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
#print("We can even do maths inside, too:")
#cheese_and_crackers(10 + 20, 5 + 6)
#
#print ("And we can combine the two, variables and math:")
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#


def sandwiches_and_drinks(sandwich_count, drink_count):
    print ("I would like to have {} sandwiches".format(sandwich_count))
    print ("And can I also please get {} drinks\n".format(drink_count))
sandwiches_and_drinks(30, 40)

test_sandwich_count = 10
test_drink_count = 25 

sandwiches_and_drinks(test_sandwich_count, test_drink_count)

sandwiches_and_drinks (30+test_sandwich_count, 40+test_drink_count)