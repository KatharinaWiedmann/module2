# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:31:07 2018

@author: Katharina
"""
#
##Exercise 1: Loop through a list using a for loop
#
my_shopping_cart = ["cake" +" "+ "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print(item)
#    
##Exercise 2: Update a list value 
values = [875, 23, 451]
for val in values:
    print('-------> ', (val+50))
#
##Exercise 3:Create your own list 
values = ['this', 55, 'that']
for item in values:
    print('*****', item)    
        
#    
##Exercise 4: Looping through Strings     
for char in "This is interesting".split('i'):
    print(char)
#    
##Exercise 5: Loop through a tuple
my_colours = ('blue', 'green', 'yellow', 'red')
for item in my_colours:
    print('########',item)
#          
##Exercise6: Loop through a dictionary
info_metals = {'iron': (7.8, 10, 22), 'gold': (19.3, 210, 13), 'zinc': (7.13, 23, 54), 'lead': (11.4, 7, 98)}
metals = list(info_metals.keys())
metals_in_order = sorted(info_metals.items(), key = lambda s:s[1][1], reverse = True)


##Option1
for var in metals_in_order:
    print(var[0], var[1][1])
#    
##Intro for Option2 
#for names, info in metals_in_order:
#    print(names, info)
#    
##Option2
for names, info in metals_in_order:
    print(names, info[1])
#
##Option3 (nested and therefore not very good!)    
for metals in info_metals:
    print(metals, info_metals[metals][1])
#    
##Exercise7
#for metal in metals:
#    print('{0:>8} = {1:5.1f}'.format(metal, info_metals[metal]))
#
#
#
##Exercise 8: COMBINING FOR LOOP AND IF STATEMENT 
#print('Combining for loop and if statement')
##Opion1
for var in metals_in_order:
    if var[1][0] > 8:
        print(var[0], var[1][0])
#
##Option2
for names, info in metals_in_order:
    if info[0]> 8:
        print(names, info[0])
#
##Option3
for metals in info_metals:
    if info_metals[metals][0] > 9:
        print(metals, info_metals[metals][0])
#
#
##Exercise8:
colours = ['red', 'green', 'red', 'green', 'blue', 'green', 'green']

d = {}
for item in colours:
    if item not in d:
        d[item] = 1
        print(d, 'first time')
    else:
        d[item] = d[item] + 1
        print(d)
#
#        
#        
#
##Exercise9: Design a sum function 
#
values = [3, 12, 9]
total = 0

for val in values:
    total += val 
print('TOTAL:' , total)
#
#
#Shopping-cart:

shopping_items = {}
shopping_items['jacket'] = ('blue', 39)
shopping_items['bag'] = ('black', 69)
shopping_items['shoes'] = ('yellow', 110)

total1 = 0
print(shopping_items)
#
for eachthing in shopping_items.items():
    total1 += eachthing[1][1]
print('Total', total1)
##    
#
#
#
#
#
#
#
#
#
#
#
christmas_wish_list = {}
christmas_wish_list['headphones'] = 149
christmas_wish_list['jewellery'] = 139
christmas_wish_list['speakers'] = 159
print(christmas_wish_list)
total = 0 

for eachitem in christmas_wish_list.items():
    total += eachitem[1]
    if total < 400:
        print(eachitem, total)
#



christmas_list = {}
christmas_list['candy'] = 6
christmas_list['chocolate'] = 2
christmas_list['gingerbread'] = 9
print(christmas_list)

for item in christmas_list.items():
    if item[1] >= 4:
        print('Yay I have received', item[1], item[0])
    elif item[1] < 4:
        print('Nooo, I want more - I only received', item[1], item[0])
#        
#
#
#
##Exercise10: Using a loop with index values
#Exercise11:Using a loop with a range function 
values = [3, 12, 9]
for index in range(0, len(values), 2): 
    values[index] = values[index] * 2
    print(values[index])
#print(values[index])
#
##Exercise12: Using a break in a for loop 
numbers = [1, 40, 5, 101, 60, 7]

for val in numbers:
    if val < 100:
        print(val)
    elif val > 100:
        print(val,'It will break here')
        break


#Exercise13: Nested loops
#Option1
outer_vals = [1, 2, 3]
inner_vals = ['A','B','C']

for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)
        
#Option2
d = {}
for oval in [1, 2, 3]:
    print(oval)
    for ival in ['A', 'B', 'C']:
        d[oval] = ival 
        print(d)
      
        
        
#Exercise14: Multiplication with a for loop 
#OWN TRY  
#outer_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
#inner_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     
#for oval in outer_vals:
#    print()
#    for ival in inner_vals:
#        print(oval*ival )
        
#book
for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(i*j), end='')
    print('\n')
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












