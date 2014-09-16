def readstreams(lst):
    for i in range(3): 
        print "give stream"
        s = read()
        lst.extend(s.split(' '))
        
    return sorted(lst)

def read()
