import random
lst = [random.randint(1,10) for i in range(0,10)]
print lst,"lst"
print sorted(lst),"sorted(lst)"

lst = [random.randint(1,10) for i in range(0,10)]
print lst,"lst"
print lst.sort(),"lst.sort()"
print lst,"lst"

for i in reversed(range(10)): print i
for i in range(10)[::-1]: print i

lst = [random.randint(1,10) for i in range(0,10)]
print lst,"lst"
print sorted(lst,reverse=True),"sorted(lst,reverse=True)"

lst = ['aaaa','e','bbbbbbbbbbb','cc','']
print lst,"lst"
print sorted(lst),"sorted(lst)"
print sorted(lst,key=len),"sorted(lst,key=len)"
print sorted(lst,key=lambda a:-len(a)),"sorted(lst,key=lambda a:-len(a))"
