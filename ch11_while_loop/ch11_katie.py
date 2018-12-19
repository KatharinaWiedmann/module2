# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:11:40 2018

@author: Katharina
"""
#exercise 1 :Repeated division
x = 33
while x >= 1:
    print(x, ':', end='')
    x = x / 2
print(x)
    
    
 
#exercise 2 : Triangular number    
n = 5 
sum = 0
while n > 0 :
    sum = sum + n
    n = n - 1 
# as soon as n !> 0 will print the sum, which is the triangular number 
print(sum)
    

# exercise 3 : marks
#Initializing first 
mark = 1

while mark > 0:
    mark = int(input('Enter mark: ')) 
    while mark > 0: 
        mark = int(input('Please type in your mark (1-100) here: '))
        if mark >= 70:
            print('Well done - firt class!')
        elif mark >= 40:
            print('That\'s alright, a pass!')
        elif mark <= 30:
            print('Oh no, you failed this class')
            break


        

#exercise 4: Using break statement in a while loop 
i = 55
while i > 10:
    print(i)
    i = i* 0.8
    if i == 35.2 :
        break
#
#
##exercise 5: 
##when not comparing anything but you still want to loop unil a condition is met 
while True:
    name = input('Enter name: ')
    if name == 'done':
        break
    print('Hello', name)
#    







