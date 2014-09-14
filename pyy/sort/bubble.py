def bubblesort(lst):
    passes = len(lst)-1
    exchanges = True
    while passes > -1 and exchanges:
        exhanges = False
        for i in range(passes):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                exchanges = True
        passes -= 1
    return lst

import random
lst = [random.randint(1,100) for _ in range(10)]
print lst,bubblesort(lst)

