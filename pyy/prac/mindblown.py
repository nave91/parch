class A:
    s = 20
    def __init__(self):
        print "aasd in A__init__"
    def __len__(self):
        return 7
a = A()
print len(a),"len(a)"
