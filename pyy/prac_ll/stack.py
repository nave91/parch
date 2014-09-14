class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        
    def pop(self):
        return self.items.pop()
