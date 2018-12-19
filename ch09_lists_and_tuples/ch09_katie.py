## -*- coding: utf-8 -*-
#"""
#Created on Thu Dec 13 09:29:12 2018
#
#@author: Katharina
#"""
##task1: Create a list 
my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]
print(x)
print(x[1])
print(x[3][1])


##task2: modify a list 
x.remove(my_favourite_fruits)
print(x)
x[1] = 'and'
print(x)
x.append('hello')
print(x)



##task3: Modify + Slice a list 
a = ['the', 'cat', 'sat']
print(a)
b = ['on', 'the', 'mat']
print(b)
c = a + b
print(c)
print(set(a+b))
#set --> unordered collection of unique elements 
y = c[-5:-3]
print(y)
#counts from the right to left but prints from left to right
#
print(c[2:5])



#task 4: Sorting lists 
x1 = [7, 11, 3, 9, 2]
print(x1)
print('-------generic sort------ will make a new sorted list')
y1 = sorted(x1)
print(y1)

print('--------object.method.sort-----------will sort the list')
x1.sort()
print(x1)



#OWN NOTES TO SORTING LISTS 

#f = ['a','v', 'l', 'k']
#print(f)
##method1
#
##f.sort()
##print(f)
#
#f.sort(reverse = True)
#print(f)
#
##method2
##y = sorted(f)
##print(y)
##
##w = sorted(f, reverse = True)
##print(w)
#
#m = [3, 8, 9, 0, 6,]
#print(m)
#
#m.sort()
#print(m)
#
#print('-------generic sort------')
#x = ['ab', 'cs', 'lm', 'hu', 'op', 'hw']
#y = sorted(x)
#print('now x is', x)
#print('now y is', y)
#
#print('--------object.method.sort-----------')
#x.sort()
#
#print('now x is', x)
#y = x.sort()
#print('now y is', y)
#


#task5: Comparing tuples and lists 
#LISTS
a = [0,1,2,3,4,5,6,7]
del a[-1]
print(a)
print(a[1:3])
a[5] = 100
a.append('z')
print(a)


#TUPLES
b = (0,1,2,3,4,5,6,7)
print(b)
#del b[-1]
#b.append('z')
print(b)
#Not possible as immutable!
#
##change a tuple into a list - make a copy and save it in new variable(p)
p = list(b) 
p.append('o')
print(p)





#task6: Create a list of tuples
a = [ 50, 7, 9, 2, 22, 99, 72, 30, 90, 2 ]
b = (33, 56, 74, 2424, 93, 3, 8, 39)
my_favourite_fruits = ['ball', 'haus', 'banana']
x = ['ow', 'zs', 'hd', 'ab','cs']
z = ['ab', 'mk', 'gh', 'cs', 'uw']
y = sorted(x)

y[0] = 'zz'

x2 = [('j', 3, z),('f', 1, y),('q', 2, x)]

print(sorted(x2, key = lambda s: s[1]))
print()

print(sorted(x2, key = lambda s: s[2]))
print()

print(sorted(x2, key = lambda s: s[2][0][1]))
print()

print(sorted(x2, key = lambda s: s[2][3][1]))
print()

print(sorted(x2, key = lambda s: s[2][1][0]))
print()
















































