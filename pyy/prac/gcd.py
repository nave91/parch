#Example gcd

def gcd(n1,n2):
    n1,n2=max(n1,n2),min(n1,n2)
    for i in range(n2,0,-1):
        if n1%i == 0 and n2 %i == 0:
            return i

def best_gcd(n1,n2):
    n1,n2=max(n1,n2),min(n1,n2)
    while n1%n2 != 0:
        oldn1,oldn2 = n1,n2
        print n1,2
        n1 = n2
        n2 = oldn1%n2
    return n2

print gcd(24,9)

print best_gcd(100,90)

import fractions

print fractions.gcd(24,9),"fractions.gcd(24,9)"
