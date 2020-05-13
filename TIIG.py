# -*- coding: utf-8 -*-
"""

@author: Raj Kishore Patra

"""

''' This program generates Random Irish Insults '''
''' The Subject, adjectives, nouns and predicates are stored as CSV files in
    working directory. Add more Insults if you think something is missed out.'''
    
import random
import time
import csv

def insult(n):
    
    insults = []
    
    files = ['subject.csv', 'adjective.csv', 'noun.csv', 'predicate.csv']
    for file in files:
        with open(file, newline='') as f:
            reader = csv.reader(f)
            li = list(reader)
            
        flatten = []
        for sublist in li:
            for item in sublist:
                flatten.append(item)
        insults.append(flatten)
    
    subject = insults[0]
    adjective = insults[1]
    noun = insults[2]
    predicate = insults[3]
    
    print("{} Irish insult(s), coming up...\n".format(n))
    time.sleep(1)
    
    for i in range(n):
        
        print(random.choice(subject)+' '+
              random.choice(adjective)+' '+
              random.choice(noun)+' '+
              random.choice(predicate)+'.')
        
if __name__ == '__main__':
    insult(int(input("How many insults do you need? \n")))