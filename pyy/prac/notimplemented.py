class Base():
    
    @property
    def example(self):
        raise NotImplementedError("subclass should implement this fucker!")

b = Base()
#b.example()
print "cannot do b.example()"


class A:
    wow = NotImplemented
    def __lt__(self,a):
        raise NotImplementedError("wow")

    def __gt__(self,a):
        raise NotImplemented

#A() < A()
print "cannot do A() < A()"
A() > A()
a = A()
print a.wow 
