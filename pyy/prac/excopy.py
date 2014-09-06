#Example for shallow vs deep copy
import copy

mat = [[i for i in range(1,4)] for i in range(1,4)]

print mat,", #mat = [[i for i in range(1,4)] for i in range(1,4)]"
print "shallow copy"
matcopy1 = copy.copy(mat)

print matcopy1, "matcopy1 = copy.copy(mat)"

matcopy1[0][0] = 1234
print "matcopy1[0][0] = 1234"
print matcopy1,"=matcopy1"
print mat,"=mat"

print "deep copy"
matcopy2 = copy.deepcopy(mat)
print "matcopy2 = copy.copy(mat)"
matcopy1[1][1] = 1234
print "matcopy1[1][1] = 1234"
print matcopy2,"=matcopy1"
print mat,"=mat"

