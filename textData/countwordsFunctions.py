# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:17:06 2019

@author: Katharina
"""

#Task1: Creates a dictionary
def countWords(filename, newlist):
    mobyDictionary = {}
    file = open(filename, "r")
#every line is string
    for line in file:
#convert every line into a list 
        linelist = line.split()

        for item in linelist:
            if item not in newlist:
                if item in mobyDictionary:
                    mobyDictionary[item] += 1
                else:
                    mobyDictionary[item] = 1
                       
    return mobyDictionary


#Task2: Orders existing dictionary

def printTop20(mobyDictionary):
    
    newDic = sorted(mobyDictionary.items(), key=lambda kv: kv[1], reverse = True)
    print(newDic[0:20])
    

#Task3: Makes a new list with stopwords without whitspace 
def readStopWords(stopwords):
    stops = open(stopwords, "r")
    newlist = []
    for line in stops:
        #deletes white space
        word = line.strip()
        
        if word not in newlist:
            newlist.append(word)           
    return (newlist)
        





























