import string,random
import sys

def generate():
    return "".join([random.choice(string.lowercase+" ") for _ in range(28)])

def score(got,want):
    if got == want: return 100
    else: 
        score = 0
        for i in range(len(got)): 
            if got[i] == want[i]: score += 1
        return score

def run():
    want = "methinks it is like a weasel"
    count = 0
    m = 10000
    ms = ''
    while True:
        got = generate()
        s = score(got,want)
        if  s == 100: 
            print "Wow!"
            sys.exit()
        else:
            count +=1 
            if min(m,s) == s and s != 0: 
                m = s
                ms = got
            if count%1000 == 0: print m,ms
 
if __name__ == "__main__":
    run()
