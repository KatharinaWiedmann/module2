# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:26:22 2018

@author: Katharina
"""
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')


more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #takes out first item from more_stuff and assigns it to next_one
    print("Adding:", next_one)
    stuff.append(next_one) #appends next_one item to stuff
    print("There's {} items now.".format(len(stuff)))
    
print("There we go:", stuff)

print("Let's do some things with stuff.")
print (stuff[1])
print(stuff[-1])
print(stuff)
#print(stuff.pop(2))
print(' '.join(stuff))
print('#'.join(stuff))