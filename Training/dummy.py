def display():
    print("Having a wonderful day")
    print(__name__)

class sample:
    namevar = None
    def __init__(self, name):
        self.namevar = name
    
    def view(self):
        print(self.namevar)