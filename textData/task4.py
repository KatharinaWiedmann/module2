# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:18:20 2019

@author: Katharina
"""

filename = "george02.txt"
filename1 = "george01.txt"
stopwords = "stopwords.txt"



# Converts text into list and deletes stop words 
text_as_list_1 = []
def converting_first_text(filename, stoplist):
    file = open(filename, "r")
#every line is string
    for line in file:
        line_without_whitespace = line.strip()
        line_converted_in_list = line_without_whitespace.split()
#        print(line_converted_in_list)
        for item in line_converted_in_list:
            if item not in stoplist:
                text_as_list_1.append(item)
    return (text_as_list_1)


# Creates list with stopwords 
def readStopWords(stopwords):
    stops = open(stopwords, "r")
    stoplist = []
    for line in stops:
        #deletes white space
        word = line.strip()
        
        if word not in stoplist:
            stoplist.append(word)           
    return (stoplist)

stoplist = readStopWords(stopwords)      

        
text_as_list_1 = converting_first_text(filename, stoplist)


# Converts text into list and deletes stop words 
def converting_second_text(filename1, text_as_list_1, stoplist):
    file = open(filename1, "r")
    text_as_list_2 = []
    for line in file:
        line_without_whitespace = line.strip()
        line_converted_in_list = line_without_whitespace.split()
#        print('--------------------------')
        for item in line_converted_in_list:
            if item not in stoplist:
                text_as_list_2.append(item)

    return (text_as_list_2)

text_as_list2 = converting_second_text(filename1, text_as_list_1, stoplist)   

#Converts in new list without doubles and counts unique words
def text_as_list_1_unique(text_as_list_1):
    count1 = 0
    text_as_list_1_unique = []
    for item in text_as_list_1:
        if item not in text_as_list_1_unique:
            text_as_list_1_unique.append(item)
            count1 += 1
#    print (text_as_list_1_unique, count1)        
    return (text_as_list_1_unique, count1)

text_as_list_1_unique = text_as_list_1_unique(text_as_list_1) 
    

#Converts in new list without doubles and counts unique words
def text_as_list2_unique(text_as_list2):
    count2 = 0
    text_as_list2_unique = []
    for item in text_as_list2:
        if item not in text_as_list2_unique:
            text_as_list2_unique.append(item)
            count2 += 1
#    print (text_as_list2_unique, count2)        
    return (text_as_list2_unique, count2)

text_as_list2_unique = text_as_list2_unique(text_as_list2) 


#Counts the items the both unique lists have in common 
def common_words_in_unique_list(text_as_list_1_unique, text_as_list2_unique):
#    print(text_as_list_1_unique[0])
#    print(text_as_list2_unique[0])
    list_words_in_both_texts = []
    count_both = 0
#    for item in text_as_list_1_unique[0]:
#        if item in text_as_list2_unique[0]:
#            list_words_in_both_texts.append(item)
#            count_both += 1
#    print(list_words_in_both_texts,count_both)
#    
    for item in text_as_list2_unique[0]:
        if item in text_as_list_1_unique[0]:
            list_words_in_both_texts.append(item)
            count_both += 1
    print('words shared in both texts:', count_both)
    return count_both 
#    print(list_words_in_both_texts,count_both)



count_both = common_words_in_unique_list(text_as_list_1_unique, text_as_list2_unique)

#Divides the words in common and words in total 
def calc_percentage(text_as_list_1_unique, text_as_list2_unique, count_both):
    print(text_as_list_1_unique[1])
    print(text_as_list2_unique[1])
    print(count_both)
    
    unique_words_text1 = int(text_as_list_1_unique[1])
    unique_words_text2 = int(text_as_list2_unique[1])
    
    overlap_dec = count_both/(unique_words_text1 + unique_words_text2)
    overlap_percent = overlap_dec* 100
    
    print('The two texts overlap {} %'.format(overlap_percent))
    
calc_percentage(text_as_list_1_unique, text_as_list2_unique, count_both)



























