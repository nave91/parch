def consec(s):
    if len(s) == 0: return None
    m = 1
    char = ''
    sim = ''
    count = 1
    similar = False
    for _i,i in enumerate(s):
        if _i == 0:
            char = i
            continue
        elif s[_i] == s[_i-1]:
            count+=1
        else:
            count = 1
        if count > m:
            m = count
            char = i
            similar = False
        if count == m and not similar and char == s[_i]:
             char = i
        else:
            similar = True
                
        
    
    return m,char

print consec('abcddde')
