#property
'''
class P:
    def __init__(self, name):
        self.name = name
    
    @property
    def Name(self):
        return "Mr." + self.name
    
    @Name.setter
    def Name(self, name):
        self.name = name
        
f = P("sample")
print(f.Name)
f.Name = "Sridhar"
print(f.Name)
'''
#time
'''
import time

def measure(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def power(rng):
    return [x**2 for x in range(rng)]

measure(lambda: power(5000000))
'''
#regex
#.* 1 or any
#.+ 1 or more
'''
import re

txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)

x = re.split("\s", txt)
print(x)

s = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM'
lst = re.findall('\S+@\S+', s) 
print(lst)
'''
#logging
'''
debug
info
warning
error
critical
'''
'''
import logging
logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger("7.py")
log.warning("Sample message")
'''
'''
import logging
logging.basicConfig(level = logging.DEBUG, filename="log.txt")
log = logging.getLogger("7.py")
log.warning("Sample message")
log.debug("Debug information")
'''
#Iter tools
'''
from itertools import repeat
for i in repeat("happy",10):
    print(i)
'''
'''
from itertools import count
for i in count(1):
    if(i == 6):
        break
    print(i)
'''
'''
from itertools import count
for i in count(1,2):
    if(i == 11):
        break
    print(i)
'''
#iter and next
'''
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#print(next(myit))
'''
#generators
#yield
'''
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3 

for i in simpleGeneratorFun():
    print(i)
'''
#xrange only in python 2
for i in xrange(1,10):
    print(i)