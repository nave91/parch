def revstr(s):
    if len(s) == 0: return ""
    if len(s) == 1: return s
    else: return s[-1]+revstr(s[:-1])

print revstr('crying')
