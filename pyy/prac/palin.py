def palin(s):
    length = len(s)
    if length%2 == 0:
        r = length//2 
        l = r-1
    else:
        l = length//2-1
        r = length//2+1
    while l>-1 and r<length:
        if s[l] != s[r]:
            return False
        l -= 1
        r += 1
    return True

def palin_best(s):
    if str(s) == str(s[::-1]): return True
    else: return False
    
print palin('radar')

import time

for func in [palin,palin_best]:
    st = time.time()
    func('ab'*1000000)
    et = time.time()
    print (et-st)*1000
