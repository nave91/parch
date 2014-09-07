import itertools

print list(list([123])),"#"*5,"Interesting","list(list([123]))"

print [i for i in itertools.permutations("cat")],"#*5","[i for i in itertools.permutations('cat')]"
print [i for i in itertools.permutations("123")],"#*5","[i for i in itertools.permutations('123')]"

for i in range(3):
    print 

print "#check for other way to permute recursively"

import sys
def permute(s,step=0):
  if step == len(s): print "".join(s)
  for i in range(step,len(s)):
    st = [c for c in s]
    st[i],st[step] = st[step],st[i]
    permute(st,step+1)

permute('cat')

for i in range(3):
    print 


print [i for i in itertools.permutations("cat",2)],"#*5","[i for i in itertools.permutations('cat',2)]"
print [i for i in itertools.permutations("123",2)],"#*5","[i for i in itertools.permutations('123',2)]"

for i in range(3):
    print 

def permute(s,n,step=0):
  if step == len(s): return ["".join(s[:n])]
  res = []
  for i in range(step,len(s)):
    st = [c for c in s]
    st[i],st[step] = st[step],st[i]
    res.extend(permute(st,n,step+1))
  return res
def combi(s):
    xs = []
    for x in range(1,len(s)+1):
        xs.extend(permute(s,x))
    print xs
combi('cat')

def permutations(A, B = ''):
    assert len(A) >= 0
    assert len(A) == len(set(A))
    if len(A) == 0:
        return [B]
    else:
        res = []        
        for i in range(len(A)):
            res.extend(permutations(A[0:i] + A[i+1:], B + A[i]))

        return res

print permutations('word')
