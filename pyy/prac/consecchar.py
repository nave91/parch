def consec(s):
    print s
    m = -1
    char = ''
    count = 0
    for _i,i in enumerate(s):
        print i,count,m
        if _i == 0: 
            count += 1
            continue
        if s[_i] == s[_i-1]:
            count += 1
        else:
            count = 0
        if count > m: 
            m = count
            char = i
    print m,char
consec('aaabbccccccccccc')
