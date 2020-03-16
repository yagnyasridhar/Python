#break and continue
'''
lst = [2,4,5,6,7]
for i in lst:
    if(i % 2 == 0):
        print(i)
        continue
    else:
        print(i)
        break;
'''
#accidental tuple
'''
t = "sample",
print(t)
'''
#lottery
'''
lottery_numbers = {1,3,4,9,15}
players = [
    {
        'name': 'Rolf',
        'numbers': {1, 3, 8, 22, 21}
    },
    {
        'name': 'Jose',
        'numbers': {4, 9, 10, 12, 15}
    }
]

name = players[0]['name']
numbers = players[0]['numbers'].intersection(lottery_numbers)
print('Player {name} got {amount} numbers right.'.format(name=name, amount=len(numbers)))
 
name = players[1]['name']
numbers = players[1]['numbers'].intersection(lottery_numbers)
print('Player {name} got {amount} numbers right.'.format(name=name, amount=len(numbers)))
'''
#serialization with pickle
'''
import pickle
class Animal:
    mamDict = {}
    name = None
    legs = None

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def load(self):
        self.mamDict[self.name] = self.legs

Dog = Animal("Dog", 4)
Crow = Animal("Crow", 2)

pickObj = pickle.dumps(Dog)
print(pickObj)

dog = pickle.loads(pickObj)
print(dog.name)

dumpFile = open('examplePickle.txt', 'ab')
piobj =  pickle.dump(Crow, dumpFile)
dumpFile.close()

dfile = open('examplePickle.txt', 'rb') 
crow = pickle.load(dfile)
dfile.close()
print(crow.legs)
'''
#json serialization and deserialization
'''
import json

class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
 
student = Student(first_name="Sridhar", last_name="Shankar")
json_data = json.dumps(student.__dict__)
print(json_data)

s = json.loads(json_data)
print(s["first_name"])
'''
#os
'''
import os
print(os.getcwd())
'''
#prety print
'''
import pprint
pprint.pprint("Sample example",indent=4,width=12)
'''
#calender
'''
import calendar as cd 
t=cd.TextCalendar(0)
print(t.formatmonth(2018,12))
'''
#explain virtual env
'''
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.venv\scripts\activate
'''
#parameters
'''
import math
def func(a,b=0):
    if(b == 0):
        return math.factorial(a)
    else:
        return a * b

print(func(12))
'''
#lamda parameter:return 
'''
def divide(x,b):
    return x / b

print(divide(10,5))

div = lambda x, y: x / y
print(div(20,4))
'''
# function as variable
'''
import math
def fun(a):
    return math.factorial(a)

def display(d):
    print(d(12))

display(fun)
'''