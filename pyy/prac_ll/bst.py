class TreeNode:
   def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = Treenode(key,val)
        
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.hasLeftChild())
            else:
                currentNode.left = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.hasRightChild())
            else:
                currentNode.right  = TreeNode(key,val,parent=currentNode)
    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root.key == key:
            return self.root
        else:
            return self._get(key,self.root)

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key: return currentNode
        elif key < currentNode.key:
            return self._get(key,val,currentNode.leftChild)
        else:
            return self._get(key,val,currentNode.rightChild)


    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self.get(key):
            return True
        else:
            False
            
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -=  1
            else:
                raise KeyError('Key not found')
        elif self.size == 1:
            self.root = None
            self.root = 0
        else:
            raise KeyError('Key not found')
        
    def __delitem__(self,key):
        self.delete(key)
        
    def remove(self,currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            self.spliceOut()
            currentNode.key = succ.key
            currentNode.value = succ.value

        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.value,
                                                currentNode.leftChild.hasLeftChild(),
                                                currentNode.leftChild.hasRightChild())
            else: 
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild  = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild  = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.value,
                                                currentNode.rightChild.hasLeftChild(),
                                                currentNode.rightChild.hasRightChild())

            
            
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.leftChild():
            current = current.leftChild
        return current
        
    def spliceOut(self):
        if self.isleaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
            else:
                if self.isRightChild():
                    self.parent.rightChild = self.rightChild
                else:
                    self.parent.leftChild = self.rightChild

        
