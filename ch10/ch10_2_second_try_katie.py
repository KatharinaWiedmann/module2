# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:12:44 2018

@author: Katharina
"""


def addAnotherClassMate(phoneBook):
    print('Would you like to add another class mate? Y/N' )
    option = input()
    if option == 'Y':
        phoneBook = addClassMate(phoneBook)
    elif option == 'N':
        choosingWhatToDo()

def addClassMate(phoneBook):
    name = input('Please type in your name ').title()
    luckyNo = int(input('Please give me your lucky number '))
    postCode = input('Please give me your post code ')
    town = input('Please type in your town ')
    age = int(input('Please give me your age '))
    value = [luckyNo, postCode, town, age]
    phoneBook[name] = value
    print('This is your current phonebook', phoneBook)
    addAnotherClassMate()
    return phoneBook
    

def sortByName():
    phoneBooksortedbyName = sorted(phoneBook.items(), key = lambda s:s[0])
    print(phoneBooksortedbyName)
    choosingWhatToDo()


def sortByLuckyNumber():
    names = list(phoneBook.keys())
    names.sort(key = lambda k:phoneBook[k][0])
    print(names)
    print('Would you rather see all the information sorted by LuckyNumber? Y/N ')
    option = input()
    if option == 'Y':
        phoneBooksortedbyLuckyNumber = sorted(phoneBook.items(), key = lambda s:s[1])
        print(phoneBooksortedbyLuckyNumber)    
        choosingWhatToDo()
    elif option == 'N':
        choosingWhatToDo()


def sortByTown():
    phoneBooksortedbyTown = sorted(phoneBook.items(), key = lambda s:s[3])
    print(phoneBooksortedbyTown)
    choosingWhatToDo()

#sort by what?
def sortBy():
    print('If you want to sort the phonebook by Name type in 1 ')
    print('If you want to sort the phonebook by Lucky Number type in 2 ')
    print('If you want to sort the phonebook by Town type in 3 ')
    option = input()
    if option == '1':
        sortByName()
    elif option == '2':
        sortByLuckyNumber()
    elif option == '3':
        sortByTown()

def compareAge(phoneBook):
    queensAge = 92
    print('Whose age would you like to compare with the Queen\'s age? Please type in the name here: ')
    k = input()
    if k in phoneBook:
        ageDifference = queensAge - (phoneBook[k][3])
        print('You are {} years younger than the Queen.' .format(ageDifference))
        phoneBook[k].append(ageDifference)
        print(k, phoneBook[k])
        choosingWhatToDo(phoneBook)
        
    else:
        print(k, 'is not in the phonebook yet')
        print('Would you like to add this person? Y/N ')
        option = input()
        if option == 'Y':
            phoneBook = addClassMate(phoneBook)
        elif option == 'N':
            choosingWhatToDo()
            
            
        


#mainMenu
def choosingWhatToDo(phoneBook):
    print('What would you like to do?' )
    print('If you want to add a classmate type A')
    print('If you want to sort the phonebook type B')
    print('If you want to know the difference of age between a classmate and the Queen type in C')
    print('If you want to log out, type in \'Exit\'')
    option = input()
    if option == 'A':
        phoneBook = addClassMate(phoneBook)
    elif option == 'B':
        sortBy()
    elif option == 'C':
        compareAge(phoneBook)
    elif option == 'Exit':
        print('Thanks for using phonebook. Have a good day!')
        
        
        
phoneBook = {'Katie':[7, 'E8 2DF', 'London', 23], 'Pam':[5, 'BR3 1PR', 'London', 30]}
choosingWhatToDo(phoneBook)        


