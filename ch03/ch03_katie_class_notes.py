# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:58:21 2018

@author: 612383447
"""

"""print ("Please type your name:")
name = input().title()
print(" ")
#name = input("Whats your name").upper() --> this is another way of writing the first two lines 
print ("Hello {}!".format(name))
print(" ")


print("Please tell me your age:")
age = input()
print("Your are {} years old".format(age))

hometown = input("What\'s your hometown? ")
print ("Very nice. I like {}".format(hometown))

favourite_food = input("What is your favourite food {}?".format(name))
print("Awesome {}, I love {}!".format(name, favourite_food))"""

"""def hello_world():
    print("Hello World!")
hello_world()"""

def greeting():
    name = input("Please tell me your name! ")
    print("Hello {}!".format(name).title())
    print("Actually, {} is a really nice name - where is it from?".format((name).title()))
    country = input()
    print ("Oh thats nice, {}! I have heard many good things about {}!".format(name.title(), country.title()))
    return country

def parents(country):
    age_mum = input("How old is your mum? ")
    age_dad = input("How old is your dad? ")
    print("Thanks, together, your parents are {} years old!".format(int(age_mum)+int(age_dad)))
    name_mum = input("What\'s your mum\'s name? ")
    name_dad = input ("What\'s your dad\'s name? ")
    print("I see, so your mum {} , is {} years old and your dad {} , is {} years old".format(name_mum.title(), age_mum, name_dad.title(), age_dad))
    print("Are they also from {}?".format(country.title()))
    yes_or_no = input()
    print("Oh wow, that\'s so interesting!")
    
    
def hello_name():
    
    country =greeting()
    parents(country)
   
    
hello_name()
   