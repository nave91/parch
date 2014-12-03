class whatever:
    def __init__(self):
        self.i = 10
        
    def __repr__(self):
        return str(self.i)
        
    def printme(self):
        print self

w = whatever()
print w.i
w.printme()
