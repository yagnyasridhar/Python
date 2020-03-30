#ABC
'''
from abc import ABCMeta, abstractmethod

class abt(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass
class d1(abt):
    def dummy(self):
        pass
    def display(self):
        print("abstract method")
obj = d1()
obj.display()
'''
#hinting
'''
import typing
def greeting(name: str) -> str:
    return name

print(greeting(1))
print(greeting("sample"))
'''
#error handling
'''
class sample:
    def display(self):
        #print("not yet implemented")
        raise NotImplementedError("Not yet implemented")

    def add(self,a):
        if(not isinstance(a,str)):
            raise TypeError("Enter string")
        print("Hello " + a)
obj = sample()
#obj.display()
#obj.add(1)
obj.add("World")
'''
#custom error
'''
class customException(Exception):
    def __init__(self,message,code):
        self.code = code
        super().__init__(message)

raise customException("oops got an error",500)
'''
#try except finally
'''
try:
    val = 1000045456 / 0
except ZeroDivisionError:
    print("Received exception")
except Exception:
    print("all exception")
finally:
    print("All is well")
'''
#file
'''
file = open("sample.txt", mode="r")
content = file.read()
print(content)
file.close()

file = open("sample.txt", mode="a")
file.seek(0)
file.write("Appended")
file.close()

with open('sample.txt', 'w') as file: 
    file.write('hello world !') 

import os
if os.path.exists("sample.txt"):
  #os.remove("sample.txt")
  print("File exist")
else:
  print("The file does not exist")
'''
#argument unpacking
'''
t = [("sridhar", 33)]

class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"{self.name} is {self.age} old")

for data in t:
    info(*data).display()
'''
#map
'''
def addition(n): 
    return n + n 
  
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 
'''

#dequeue
'''
from collections import deque

friends = deque(["bhuvanesh", "Rajesh"])
friends.appendleft(("Kaushik"))
print(friends)
friends.popleft()
print(friends)
'''