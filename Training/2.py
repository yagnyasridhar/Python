#input 2 numbers
'''
status = True
a = None
b = None
c = None

def checkNumber():
    if(a.isnumeric() and b.isnumeric()):
        return False
    else:
        return True

while(status):
    a = input("Enter a number")
    b = input("Enter a number")
    status = checkNumber()
    c = int(a) * int(b) % 10

print(c)
'''
#dict
'''
thisdict = {1:123,2:234}
print(thisdict[1])
thisdict = {"Name":"Sridhar", "ID":"40207711"}
print(len(thisdict))
if("Name" in thisdict):
    print("yes")
if("Sridhar" in thisdict.values()):
    print(thisdict.values())
for str in thisdict.values():
    print(str)
for str in thisdict.keys():
    print(str)
for str in thisdict:
    print(str)
thisdict["Gender"] = "Male"
thisdict["Mobile"] = 9003299363
thisdict[40207711] = "Sridhar"
print(thisdict)
thisdict.pop(40207711)
del thisdict["Mobile"]
print(thisdict)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for str1 in myfamily:
    for str2 in myfamily[str1].values():
        print(str2)
'''
#import
'''
import dummy as d
d.display()
print(__name__)

from dummy import sample 
obj = sample("sridhar")
obj.view()
'''
#set
'''
d = { 1,2,2,3,4,5}
print(d)
list1 = [1,2,3,4,5,1,2,3,4,5]
k = set(list1)
print(k)
list1 = list(k)
print(list1)
print(d)
d.pop()
print(d)
d.remove(5)
print(d)
d.discard(5)
'''
#frozenset
'''
d = frozenset({1,2,3,4,4,4,4})
print(d)
'''
#bytes
'''
x = bytes(4)
print(x)
x = bytearray(100)
print(x)
'''
#random
'''
from random import randint
print(randint(0,100))
'''
#memoryview
'''
x = memoryview(b"Hello")
print(x)
print(x[0])
'''
#inbuilt functions
'''
x = ascii("My name is Ståle")
print(x)
'''
#math
'''
import math
x = math.cos(5)
print(x)
'''
#cmath
'''
import cmath
x = cmath.cos(5)
print(x)
'''
#matrix
'''
data = [[1,2,3], [4,5,6],[7,8,9]]
print(data)
import numpy as np
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B      # element wise addition
print(C)
'''

