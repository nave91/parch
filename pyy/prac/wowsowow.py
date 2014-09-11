print True

True = "wow"
print True,"Printing True"

True = False
print True,"Printing True..what?"

class Some:
    k = "wow, am I inside Some"
    print __name__,"wait I am not inside any function"
    def __init__(self):
        print __name__,"Im inside __init__"
    def smalls(self):
        return __name__,"Im inside smalls"
W = Some
s = W()
print s.k
print __name__
print s.smalls
print s.smalls()
