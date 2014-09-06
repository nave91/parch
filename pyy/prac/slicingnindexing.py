#Example of slicing and indexing lists

#dividing strings

a = [i for i in range(0,10)]

print a
print a[:5],"a[:5]"
print a[5:],"a[5:]"
print a[1:3],"a[1:3]"
print a[::1],"a[::1]"
print a[1:8:2],"a[1:8:2]"
print a[1:8:-2],"a[1:8:-2]"
print a[5:8:-2],"a[5:8:-2]"
print a[-1],"a[-1]"
#When negative lst[last:first:negative]
print a[:-1],"a[:-1]"
print a[0:-1],"a[0:-1]"
print a[::-1],"a[::-1]"
print a[::-2],"a[::-2]"
print a[-1:2:-2],"a[-1:2:-2]"
print a[-1:3:-2],"a[-1:3:-2]"
