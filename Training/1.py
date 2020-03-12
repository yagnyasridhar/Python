'''
print("Hello, World!")
'''
#comment
#print("Hello, World!")

#indentation
'''
i = 12
if type(i) == type(1):
    print("wow")
'''
#variable
'''
i = "sample"
y = 10
print(y+i)
'''
'''
i = "awesome"
def func():
    global i 
    i = "value"
    print(i)

func()
print(i)
'''
#pass
'''
def func():
    pass

func()
'''
# data type
'''
print(type(12.3))
print(type(12j))
print(type("sasas"))
'''
#casting
'''
i = "sample"
y = 10
print(str(y)+" "+i)
'''

#string

a = "Hello, World!"
b = "hello world"
print(a.upper())
print(b.title())
print(a[0])
print(a[:4])
print(a[0:-2])
print(a.split(","))
print(a[::-1])
#list
'''
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[0:2])
thislist.append("mango")
print(thislist)
thislist.insert(1, "grapes")
print(thislist)
thislist.pop()
print(thislist)
thislist.remove("banana")
print(thislist)
list2 = ["orange"]
thislist.extend(list2)
print(thislist)
'''

#tuple
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print(thistuple[2:3])
'''
#range
'''
x = range(3, 20, 2)
for n in x:
  print(n)
  '''
#input
'''
username = input("Enter username:")
print("Username is: " + username)
'''

#formating
'''
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
'''

#palindrome
'''
str = input("Enter a string: ")
if(str == str[::-1]):
    print("palindrome")
else:
    print("not palindrome")
    '''
