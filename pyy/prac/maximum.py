import random

lst = [random.randint(1,100)*random.randint(1,100) for i in range(1,10)]

def maximum(lst):
    m = -1
    for i in lst:
        if i > m:
            m = i 
    return m


def maximum2(lst):
    for _i,i in enumerate(lst):
        for _j,j in enumerate(lst):
            if i<j: break
        if _j+1 == len(lst): return i
print lst
print maximum(lst)
print maximum2(lst)
