def sums(lst):
    s = 0
    for i in lst: s+=i
    return s

def sums1(lst):
    if not lst: return 0
    return lst[0] + sums1(lst[1:])

import random
lst = [random.randrange(0,111) for _ in range(0,500)]

import time
for i in [sums,sums1]:
    st = time.time()
    i(lst)
    et = time.time()
    print (et-st)*1000  
