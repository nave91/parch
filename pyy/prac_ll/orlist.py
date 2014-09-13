class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self,data):
        self.data = data

    def setNext(self,next):
        self.next = next

    def __repr__(self):
        return str(data)

class Orlist(Node):
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        current = self.head
        prev = None
        stop = False
        while current != None and not stop:
            if current.data > item:
                stop = True
            else:
                prev = current
                current = current.getNext()
        tmp = Node(item)
        if prev == None:
            tmp.setNext(self.head)
            self.head = tmp
        else:
            tmp.setNext(current)
            prev.setNext(tmp)
    
    def search(self,item):
        current = self.head
        stop = False
        while current != None and not stop:
            if current.data == item:
                return True
            elif current.data > item:
                stop = True
            else:
                current = current.getNext()
        return False

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def remove(self,item):
        current = self.head
        stop = False
        while current != None and not stop:
            if current.data == item:
                stop = True
            else:
                prev = current
                current = current.getNext()

        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())

    def __repr__(self):
        s = ""
        current = self.head
        while current != None:
            s += str(current.data)+"->"
            current = current.getNext()
        return s[:-2]

mylist = Orlist()
mylist.add(10)
mylist.add(13)
mylist.add(29)
mylist.add(98)
mylist.add(50)
print mylist
print mylist.search(50)
print mylist
mylist.remove(50)
print mylist
print mylist.size()
