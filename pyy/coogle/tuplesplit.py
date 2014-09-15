def tupsplit(lst):
    a,b=[],[]
    for l in lst:
        a.append((l[0],l[1]))
        b.append((l[0],l[2]))
    return sorted(a+b,key=lambda y: y[1])

lst = [('a', 1, 5), ('b', 2, 4), ('c', 7, 8)]

print tupsplit(lst)
