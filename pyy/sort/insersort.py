def insersort(lst):
    for i in range(1,len(lst)):
        cur = lst[i]
        pos = i
        while pos > 0 and lst[pos-1] > cur:
            lst[pos] = lst[pos-1]
            pos -= 1
        lst[pos] = cur
    return lst

import random
lst = [random.randint(1,100) for i in range(10)]
print lst,insersort(lst)
