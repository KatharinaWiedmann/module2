# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:17:48 2019

@author: Katharina
"""

from countwordsFunctions import *


filename = "mobydick.txt"
stopwords = "stopwords.txt"


newlist = readStopWords(stopwords)
countWords(filename, newlist)

#next line is necessary so that printTop20 knows what has to be passed into the function 
mobyDictionary = countWords(filename, newlist)

printTop20(mobyDictionary)
