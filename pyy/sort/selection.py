def selecsort(lst):
    for _m in range(len(lst)-1,0,-1):
        pMax = 0
        for i in range(0,_m+1):
            if lst[i] > lst[pMax]:
                pMax = i
        lst[_m],lst[pMax] = lst[pMax],lst[_m]
    return lst

import random
lst = [random.randint(1,100) for _ in range(10)]
print lst,selecsort(lst)
