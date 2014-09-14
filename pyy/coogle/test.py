b=[i for i in range(100000)]

def solution(A):
    lst = [i for i in range(1,len(A)+2)]
    ans = list(set(lst)-set(A))
    print ans[0]
    
print solution(b)
