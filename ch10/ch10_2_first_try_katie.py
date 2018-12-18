# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:15:38 2018

@author: Katharina
"""
class phoneBookDataCollection():
    def __init__(self, name, phoneNo, luckyNo, postCode, town):
        self.name = name
        self.phoneNo = phoneNo
        self.luckyNo = luckyNo
        self.postCode = postCode
        self.town = town 

#   
          
#user1 = phoneBookDataCollection(name, phoneNo, luckyNo, postCode, town)
#user1.askForUserInput()
#phoneBookDataCollection(namex, phoneNox, luckyNox, postCodex, townx)
def askForUserInput():
        namex = input('Please tell me your name: ')
        phoneNox = input('Please type in your phone number here: ')
        luckyNox = input('Please type in your Lucky Number here: ')
        postCodex = input('Please type in your post code here: ')
        townx = input('Please type in your town here: ')
        return namex, phoneNox, luckyNox, postCodex, townx 
    
dataFromUser = askForUserInput()
person1 = phoneBookDataCollection(dataFromUser[0], dataFromUser[1], dataFromUser[2], dataFromUser[3], dataFromUser[4])
person2 = phoneBookDataCollection(dataFromUser[0], dataFromUser[1], dataFromUser[2], dataFromUser[3], dataFromUser[4])

print('name',person1.name)
print('phoneNo', person1.phoneNo)

person = person1
person = person2

phoneBook = {}
phoneBook[person.name] = person.phoneNo, person.luckyNo, person.postCode, person.town
