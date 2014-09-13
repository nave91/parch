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
        return str(self.data)

class Unlist(Node):
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def remove(self,item):
        if self.head.data == item:
            self.head = self.head.getNext()
        current = self.head
        nextone = self.head.getNext()
        while nextone != None:
            if nextone.data == item:
                current.next = nextone.getNext()
                break
            else:
                current = current.getNext()
                nextone = current.getNext()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.getNext()
        return False

    def __repr__(self):
        current = self.head
        s = ""
        while current != None:
            s += str(current)+"->"
            current = current.getNext()
        return s[:-2]

mylist = Unlist()
mylist.add(10)
mylist.add(13)
mylist.add(29)
mylist.add(98)
print mylist
print mylist.search(10)
mylist.remove(10)
print mylist
print mylist.size()
