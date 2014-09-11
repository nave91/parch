#Example of anagram

def anagram(a,b):
    for i in a:
        if i not in b:
            return False
    return True

def worse_anagram(a,b):
    b0 = list(b)
    stillOK = True
    _a = 0
    while _a < len(a) and stillOK:
        _b = 0
        found = False
        while (_b < len(b0)) and (not found):
            if a[_a] == b0[_b]:
                found = True
            else:
                _b += 1
        if found:
            b0[_b] = None
        else:
            stillOK = False
        _a += 1
    return stillOK

def best_anagram(a,b):
    a0 = [0]*26
    b0 = [0]*26

    for i in a:
        pos = ord(i) - ord('a')
        a0[pos] += 1
    for i in b:
        pos = ord(i) - ord('a')
        b0[pos] += 1

    pos = 0
    while pos < 26:
        if a0[pos] != b0[pos]:
            return False
        pos += 1
    return True

import time
for func in [anagram,best_anagram,worse_anagram]:
    st = time.time()
    func('horse'*1000,'shore'*1000)
    et = time.time()
    print (et-st)*1000
    
print worse_anagram('horse','shore')
print anagram('horse'*100000,'shore'*100000)
print best_anagram('horse'*100000,'shore'*100000)


###Results
"""
0.155925750732
1.98006629944
1811.14697456 ----->This is big
True
True
True
"""
