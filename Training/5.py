#graphs
'''
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

print(generate_edges(graph))
'''
#classes and Inheritance
'''
class parent(object):
    def __init__(self, father, mother):
        self.Father = father
        self.Mother = mother
    
    def display(self):
        print(f"Father:{self.Father} Mother:{self.Mother}")

p = parent("Shankar","Latha")
p.display()

class child(parent):
    def __init__(self,father, mother, child):
        #super().__init__(father,mother)
        parent.__init__(self,father,mother)
        self.Son = child

    def display1(self):
        print(f"Son: {self.Son}")

c = child("Shankar","Latha","Sridhar")
c.display()
c.display1()
'''
#decorators
#static and class methods
'''
class sample:
    def __init__(self):
        self.Name = "sridhar"

    @staticmethod
    def display():
        print("Sample")

    @classmethod
    def ds1(cls):
        print("ghfgdgd")

sample().display()
sample().ds1()
'''
#diamond problem
'''
class a:
    def display(self):
        print("base class")

class b(a):
    def __init__(self):
        super().__init__()
    def display(self):
        print("derived1")
class c(a):
    def __init__(self):
        super().__init__()
    def display(self):
        print("derived2")
class d(b,c):
    def __init__(self):
        super(d,self).__init__()
    def sample(self):
        self.display()
        b.display(self)
        c.display(self)

obj = d() 
obj.sample()
'''
#repr str
'''
import datetime 
today = datetime.datetime.now() 
print(str(today))
print(repr(today))

class c:
    def display(self):
        print("sample project")
    def __repr__(self):
        return (f"{__class__}")
    def __str__(self):
        return "Helpful info"

ob = c()
print(str(ob))
print(repr(ob))
'''
#getter
'''
class CustomList:
    def __init__(self):
        self.collection = []
    
    def __getitem__(self,i):
        print("entering get")
        return self.collection[i]
        print("exiting get")
    
    def __setitem__(self,i,v):
        print("entering set")
        self.collection.insert(i,v)
        print("exiting set")

c = CustomList()
c[0] = "s"
print(c[0])
'''