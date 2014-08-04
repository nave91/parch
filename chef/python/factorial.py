t = input()
n = 0
while n < t:
    num = input()
    i = 0
    div = 5
    while num/div >= 1:
        i += num/div
        div *= 5
    print i
    n= n+1
