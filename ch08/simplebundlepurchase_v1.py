# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 04:50:08 2018

@author: Katharina
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        task = checkTask()
        if task == '1':
            displayBalance(balance)
        elif task == '2':
           if askForPhoneNumber():
               print("Your two phone numbers match")
               if checkBalance(balance) :  
                   print('Your balance is {}'.format(balance))
                   amount = topup(balance)
                   if amount < balance:
                       print("You just purchased data")
                       newBalance = calculateNewBalance(amount, balance)
                       print("Your new balance is {}.".format(newBalance))
                   else:
                       return 'Transaction failed due to insufficient balance'                
               else:
                   return ('Your balance of {} is not sufficient.'.format(balance))
           else:
               return("The phone numbers don't match - unfortunately we cannot proceed here.")
#           
           
    else:
        return 'Wrong password'
    
    #return ('not yet created')
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ') 
    if attempt == truePasscode:
        return True
    else:
        return False

def checkTask():
    askForTask = input("For checking your balance type in '1', for purchasing a data bundle type in '2'. ")
    return askForTask 
   
 
def displayBalance(balance):
    printBalance = print("Your balance is {}".format(balance))
    return printBalance

def askForPhoneNumber():
    phoneNumber1 = input("Please type in your phone number here: ")
    phoneNumber2 = input("Please type it in again: ")
    if phoneNumber1 == phoneNumber2:
        return True
    else:
        return False
         
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def topup(balance):
    amount = int(input("If you like you can purchase a data bundle worth {}. How much would you like to spend on data? ".format(balance)))
    return amount 
 
def calculateNewBalance(amount, balance):
    newBalance = balance - amount
    return newBalance
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    