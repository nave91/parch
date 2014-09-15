class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.heapsize = 0

    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i = i//2

    def insert(self,item):
        self.heapList.append(item)
        self.heapsize += 1
        self.percUp(self.heapsize)

    def percDown(self,i):
        while i*2 <= self.heapsize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc
        
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
            self.percDown(i)
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

def ran(lsts):
    bh = BinHeap()
    lens = [len(l) for l in lsts]
    ind_min = lens.index(min(lens))
    a = []
    for _l,l in enumerate(lsts):
        a.append(l[0])
    bh.buildHeap(a)
    bh.printTree()
    r = (max(bh.heapList)-min(bh.heapList[1:]))
    rang = (max(bh.heapList),min(bh.heapList[1:]))
    cnt = 0
    while len(lsts[ind_min])>0:
        m = min(bh.heapList[1:])
        for _l,l in enumerate(lsts):
            print m,l[0]
            if m == l[0]: 
                print "Aweadasd"
                lsts[_l].pop(0)
                bh.delMin()
                print bh.heapList
                if not lsts[_l]: break
                bh.insert(lsts[_l][0])
                print lsts[_l]
                break
        bh.printTree()
        print len(lsts[ind_min])
        if r > (max(bh.heapList)-min(bh.heapList[1:])):
            print r,rang
            r = max(bh.heapList)-min(bh.heapList[1:])
            rang = (max(bh.heapList),min(bh.heapList[1:]))
    return r,rang
        

lsts = [[4, 10, 15, 24, 26],[0, 9, 12, 20] ,[5, 18, 22, 30] ]

print ran(lsts)





