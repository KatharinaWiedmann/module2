# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:29:12 2018

@author: Katharina
"""

#my_favourite_fruits = ['apple', 'orange', 'banana']
#x = ['this', 55, 'that', my_favourite_fruits]
#
#x.remove(my_favourite_fruits)
#print(x)
#x[1] = 'and'
#print(x)
#
#
#x.append('hello')
#print(x)
#
#a = ['the', 'cat', 'sat']
#print(a)
#b = ['on', 'the', 'mat']
#print(b)
#c = a + b
#print(c)
#print(set(a+b))
#
#y = c[-3:-5]
#print(y)
#
#print(c[2:5])

#sorting lists 
f = ['a','v', 'l', 'k']
print(f)
#method1

#f.sort()
#print(f)

f.sort(reverse = True)
print(f)

#method2
#y = sorted(f)
#print(y)
#
#w = sorted(f, reverse = True)
#print(w)

m = [3, 8, 9, 0, 6,]
print(m)

m.sort()
print(m)




print('-------generic sort------')
x = ['ab', 'cs', 'lm', 'hu', 'op', 'hw']
y = sorted(x)
print('now x is', x)
print('now y is', y)



print('--------object.method.sort-----------')
x.sort()

print('now x is', x)
y = x.sort()
print('now y is', y)


print('---tuple vs list---')
a = [0,1,2,3,4,5,6,7]
del a[-1]
print(a[1:3])

a[5] = 100
a.append('z')
print(a)


#tuples are immutable! 
b = (0,1,2,3,4,5,6,7)
#del b[-1]
#b.append('z')
print(b)


#change a tuple into a list - make a copy and save it in new variable(p)
p = list(b) 
p.append('o')
print(p)










































