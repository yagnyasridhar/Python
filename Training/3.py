#scope
'''
a = 100
def fun():
    a = 200
    print(a)

print(a)
fun()
'''
'''
def fun():
    a =100
    def func1():
        nonlocal a
        a = 200
        b = 100
        print(a)
        print(b)
    func1()
    print(a)
fun()
'''
#identifiers
#__sub__ for –
'''
class sample:
    _i = 0
    __sa = 0
    __sam__ = 0
    def __init__(self):
        self._i = 12
        self.__sa = 1303
        self.__sam__ = 12345

obj = sample()
print(obj.__sam__)
'''
#bitwise operator
'''
print(bin(7))
print(~9)
print(2>>1)
'''
#ternary
#[on_true] if [expression] else [on_false]
'''
import random
a = random.random()
b = random.random()
print("a" if a>b else "b")
'''
#default dictionary
'''
d = {1:"sri", 2:"dhar"}
print(d)
print(d[3]) #error
'''
'''
from collections import defaultdict
def defaultValue():
    return 0
d = defaultdict(defaultValue)
d[1] = "name"
print(d[3])
print(d.keys())
'''
#ordered dictionary
'''
if({'a': 1, 'e': 5, 'd': 4, 'b': 2, 'c': 3}=={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}):
    print("wow")
from collections import OrderedDict
dic = OrderedDict([("c", 3), ("e", 5), ("a", 1), ("b", 2), ("d", 4)])
print(dic.keys())
'''
#Namedtuple 
'''
from collections import namedtuple
colors = namedtuple("colors",['red','green','blue'])
d = colors(0,1,2)
print(d.red)
'''
#enum
'''
import enum
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3

print(Days.Sun.value)
'''
#List Comprehension
'''
lst = []
for i in range(8):
    lst.append(i)
print(lst)
'''
'''
print([i for i in range(8) if i%2!=0])
print(["Even" if i%2 else "odd" for i in range(10)])
'''
#zip
'''
for i in zip([1,2,3],['a','b','c']):
    print(i)
'''
#repr
'''
msg='Hello, world!'
print(repr(msg))
'''
#counters
'''
from collections import Counter
lst = [1,2,3,4,3,2,3,4,2,3,4]
c = Counter(lst)
print(c[2])
'''
#datetime
'''
from datetime import datetime as dt
print(dt.now())
a = dt.now()
print(a.year)
'''