# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:15:50 2018

@author: 612383447
"""
#No.1 :
def print_two (*args):
    arg1, arg2, arg3 = args
    print ("arg1: {}, arg2: {}, arg3: {}".format(arg1, arg2, arg3))
    


#No.2
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
#No.3
def print_one(arg1):
    print ("arg1: {}".format(arg1))

#No. 4
def print_none():
    print ("I got nothin'.")

#Here functions are called.
print_two("Zed", "Shaw", "Let's see")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()