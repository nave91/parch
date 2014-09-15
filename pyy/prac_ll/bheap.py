class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.heapsize = 0

    def percUp(self,size):
        i = size
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i = i//2
    def insert(self,item):
        self.heapList.append(item)
        self.heapsize += 1
        self.percUp(size)

    def percDown(self,i):
        while i*2 <= self.heapsize:
            mc = self.minChild(i)
            if self.heapList[i] > heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = i*2
        
    def minChild(self,i):
        if i*2+1 > self.heapsize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.heapsize]
        self.heapsize -= 1
        self.heapList.pop()
        self.percDown(1)
        return val

    def buildHeap(self,lst):
        i = len(lst)//2
        self.heapsize = len(lst)
        self.heapList = [0]+lst[:]
        while i>0:
            self.percUp(i)
            i -= 1

    def printTree(self,i=1,step=0):
        if i == 1: 
            print self.heapList[i]
            step +=1
        if i*2 <= self.heapsize:
            print "|-"*step+str(self.heapList[i*2])
            self.printTree(i*2,step+1)
        if i*2+1 <= self.heapsize:
            print "|-"*step+str(self.heapList[i*2+1])
            self.printTree(i*2+1,step+1)


import random

lst = [random.randint(1,100) for _ in range(10)]
print lst
lst = [ 1 for _ in range(10)]
bh = BinHeap()
bh.buildHeap(lst)
bh.printTree()
