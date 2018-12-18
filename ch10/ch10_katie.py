# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:46:25 2018

@author: Katharina
"""

#d = {'bo': 50000, 'al': 20000, 7: ('Joke', 'Chen', 'Bond'), 'x' :'m', 'kj7':(5, 6, 7)}
#print(d)
#d['addmore']=900
#print(d)
#d['addmore'] += 20
#print(d)
#d['bo'] = 'willthisupdateanumbetoastring'
#print(d)
#
#print()
#
#tel = {'hien' : '111', 'harriet' : 989}
#print(tel['harriet'])
#tel['hien'] = '222'
#print(tel['hien'])
#print(tel)
#
#
##only possible to update the phone number (adding another digit), if it's a string
#tel['hien'] += '3'
#print(tel)
#
##del tel['hien']
##print(tel)
#tel_keys = list(tel.keys())
#
#print(tel_keys)
#print(tel_keys[0])
#print(tel_keys[1])
#
#if 'chen' in tel:
#    print('chen', ':', tel['chen'])
#else:
#    print('chen not found!')
#    
#    
#    
#counts = {'a': 3, 'c':1, 'b': 5}
#
#
#counts['a'] = (3, 9)
#counts['c'] = (10, 8)
#counts['b'] = (5, 7)
#counts['g'] = (8, 9)
#counts['f'] = (1, 90)
#counts['h'] = (65, 8)
#counts['j'] = (77, 8)
#
#labels = list(counts.keys())
#
#
##just shows labels, but still sorts the labels in the order of ascending numbers
##labels.sort()
#labels.sort(reverse = True, key = lambda k:counts[k])
##labels.sort(reverse = True, key = lambda k:counts[k]) --> descending order
#print(labels)
#
##returns both the key and the value
#print(sorted(counts.items(), key=lambda s:s[1][1]))
#
#print()
#print(sorted(counts.items(), key=lambda s:s[0]))





info_metals = {'iron': (7.8, 10, 22), 'gold': (19.3, 210, 13), 'zinc': (7.13, 23, 54), 'lead': (11.4, 7, 98)}

metals = list(info_metals.keys())


#only shows the names of the metals and sorts according to first value (e.g for iron 7.8)
metals.sort(key = lambda m:info_metals[m])
print(metals)

#only shows the names of the metals and sorts according to second value (e.g for iron 10)
metals.sort(key = lambda m:info_metals[m][1])
print(metals)

#shows names+ infos. treats key+value as a tuple. now sorts regarding names 
print(sorted(info_metals.items(), key = lambda kv: kv[0]))


#shows names+ infos. treats key+value as a tuple. now sorts regarding density
print(sorted(info_metals.items(), key = lambda kv: kv[1]))

print()

print('Show me the most expensive metal - descending order!')
#here key is not included in counting, modifies existing! 
metals.sort(reverse = True, key = lambda m:info_metals[m][1])
print(metals)


print('Show me the most expensive metal - descending order with all the info!')
#modifies duplicate 
print(sorted(info_metals.items(), key = lambda kv: kv[1][1], reverse = True))







































