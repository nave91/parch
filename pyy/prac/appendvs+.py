#Exmaple of append vs +

lst1 = [ i for i in range(0,100)]

lst2 = [i for i in range(0,100000)]

def appnd(lst1,lst2):
    return lst1.append(lst2)

def plus(lst1,lst2):
    return lst1+lst2

import time
for func in [appnd,plus]:
    st = time.time()
    func(lst1,lst2)
    et = time.time()
    print (et-st)*1000
