# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 09:35:42 2018

@author: Katharina
"""

class Person ():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognized!')
    
    def greetingInformal(self):
        print('Hi', self.name)
    def greetingFormal(self):
        if self.isMale == True:
            print("Hello Mr", self.name)
        elif self.isMale == False:
            print("Hello Mrs", self.name)
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome young', self.name)
        elif self.age < 30:
            self.greetingInformal()
        else:
            self.greetingFormal()
            
#IF IT IS A WIZARD WILL OVERWRITE THE FORMAL GREETING 
#SUBCLASSES INHERIT THE INIT METHOD 
class Wizard(Person):
#OVERWRITES INIT METHOD --> ONLY CHANGES GENDER --> EVERY WIZARD BY DEFAULT IS MALE 
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, 'm')
    def greetingFormal(self):
        print('Welcome, Mr ', self.name, end= ' ')
        print('- you\'re a fine wizard!')
    def spell(self):
        print('Expelliarmus!')
    
            
p1 = Person('Sophia', 12, 'f')
p2 = Person('Vincent', 25, 'm')
p3 = Person('Maximilian', 60, 'm')
p4 = Wizard('Joseph', 45, 'f')
