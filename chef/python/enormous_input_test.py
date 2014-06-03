#! /usr/lib/env python
import psyco
psyco.full()
n,k=map(int,raw_input().split())
count = 0
data = []
for i in data[1:n]:
    if int(raw_input())%k == 0:
        count += 1
print count
