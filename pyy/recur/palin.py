def palin(s):
    if len(s)<=0: return True
    else: return s[0]==s[-1] and palin(s[1:-1])

print palin('radarasdasd')
