#Best fucking permutation recursion ever

def permute(s):
    if len(s) <=1:
        yield s
    else:
        for perm in permute(s[1:]):
            for ind in range(len(s)):
                yield perm[:ind]+s[0:1]+perm[ind:]

for i in permute('cat'):
    print i

print 'cat'[:0]
