#Example to remove duplicates from a list

lst = ['aa','b','aa','cccc','b','cccc']*10

print lst

def rdup(lst):
    """ Removes Duplicates"""
    return set(lst)

def rdup1(lst):
    """People do"""
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2

def rdup2(lst):
    """ one clever fellow did"""
    seen = ()
    for i in range(len(lst)-1,-1,-1):
        it = lst[i]
        if it in seen:
            del lst[i]
        else:
            seen+=(it,)
    return lst

print rdup(lst),"rdup(lst)"
print rdup1(lst),"rdup1(lst)"
print rdup2(lst),"rdup2(lst)"

