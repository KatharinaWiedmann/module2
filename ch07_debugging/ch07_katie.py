# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:24:46 2018

@author: Katharina
"""
##script1:debugging with print statement 
#class human():
#    def __init__(self, name):
#        self.name = name#
#
#        
#    def alive(self):
#        print("Hi {}, you are a human.".format((name).title()))
#        
#class zombie(human):
#    def __init__(self, name, behaviour):
#        self.name = name
#        self.behaviour = behaviour
#        print("test1")
#        #if the code works it should print test1
#        
#    def deadbad(self):
#        print("\nYou didn't behave very well, that's why you are zombie now.")
#        print("test2")
#        #if the code works it should print test2 
#        
#    def deadgood(self):
#        print("\nEven though you have been good, everyone becomes a zombie at some point.")
#        print("test3")
#        #if the code works it should print test3
#        
#    def goodorbad(self, behaviour):
#        if behaviour == 'good':
#            print("You still invite your human friends over for lunch")   
#        elif behaviour == 'bad':
#            print("You invite your zombie friends over and serve your human friends for lunch" )
#        else: 
#            print("Please only type good or bad")
#        
#        print("test4")
#        #if the code works it should print test4
#            
#    def future_prophecy(self, behaviour, future):
#        if behaviour == 'good' and future == 'peace':
#            print("\nYou will continue inviting your friends over for lunch and you will live together in peace." )
#        elif behaviour == 'good' and future == 'war':
#            print("\nWhat? You invited your human friends over for lunch and now you want war?!")
#        elif behaviour == 'bad' and future == 'peace':
#            print ("\nYou were eating the humans before and now you want peace? Well, everyone can change their mind right?")
#        elif behaviour == 'bad' and future == 'war':
#            print ("\nYou will continue eating all the humans, until no one is there anymore.")
#        else:
#            print("\nPlease only type peace or war")
#   
#    def future_after_falling_in_love(self, future, solve_or_continue):
#        if future == 'peace' and solve_or_continue == 'solve':
#            print("\nYou never wanted war in the first place. Spread the love - everyone will live together happily ever after.")
#        elif future == 'war' and solve_or_continue == 'solve':
#            print("\nYou came to your senses after all. Everyone lives together happily after all.")
#        elif future == 'war' and solve_or_continue == 'continue':
#            print("\nAre you sure this is real love?!")
#        else:
#            print("\nPlease only type 'solve or continue'.")
#    
##asking for name, making it human and alive    
#name = input("What's your name? ")
#person= human(name)
#person.alive() 
#
#
## asking for behaviour and turning it into a zombie
#behaviour = input("Are you good or bad? ")            
#deadperson = zombie(name, behaviour)
#print('Oh no! You just turned from a human into a zombie')
#
##depending on input fromm below, wil cal either deadbad or deadgood function 
#if behaviour == 'bad':
#   deadperson.deadbad() 
#elif behaviour == 'good':
#    deadperson.deadgood()
##asks for input and also calls goodorbad function     
#deadperson.goodorbad(behaviour)
#
##asks about future, needs to have behaviour, future input as they decide on conditionals
#future = input("\nWhat do you want the future to look like? Will there be war or peace between zombies and humans? ")
#deadperson.future_prophecy(behaviour, future)
#
#
##asks for input and calls function. this one needs also the former future input and solve or continue for conditionals
#solve_or_continue = input("\nOne more question.. What if you fall in love with a human? Will this solve all the conflicts that still exist or will they continue? Please type in 'solve' or 'continue': ")
#deadperson.future_after_falling_in_love(future, solve_or_continue)
#
#print("\nThanks for playing {}. Story to continue...".format((name).title()))


#script2: Debugging with breakpoints
userInput = input('Please give a number ')
def simpleOperation(userInput):
    intInput = int(userInput)
    result1 = intInput -2 
#    print ('result1', result1)
    return result1

def nestedOperation(result1):
    result = simpleOperation(userInput)
#    print('result should be the same like result1', result)
    result2 = result*2
#    print('result2 is (result or result1)*2', result2)
    return result2
result = simpleOperation(userInput)
result2 = nestedOperation(userInput)
print(result2)


#first button: run code until the breakpoint
#second button: reun code line-by-line until breakpoint
#third button: stepping into a section (class/function)
#fouth button: step out of the section 
#fith button: go to the next breakpoint
#last button: exit debugging mode 



##OWN NOTES 
#class mother():
#    def blonde(self):
#        print("The mother has blond hair")
#        
#class father():
#    def brown(self):
#        print("The father has brown hair")
#        
#class child():
#    def __init__(self):
#        self.o1 = mother()
#        self.o2 = father()
#    def blonde(self):
#        return self.o1.blonde()
#    def brown(self):
#        return self.o2.brown()
#    def ginger(self):
#        print("But I have ginger hair")
#    
#luisa = child()
#luisa.blonde()
#luisa.brown()
#luisa.ginger()