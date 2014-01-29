#!/usr/bin/env python
import random

##Python code for lab2##
##Ques: Return a dictionary, converted to a string, 
##      showing the keys and values (where the key,
##      value pairs are sorted descending by the
##      values).

def dictostr(dic):
    string = ""
    for key in sorted(dic.keys(),reverse=True):
        string = string + str(key) + "-" + str(dic[key])+","
    return string

dic={1:'one',2:'two',3:'three'}
#print "####dictionary to string ",dictostr(dic)

##Ques: Return one item in a list, selected at random. 
##Hints: random.random and len.

def retrandom(list):
    return list[random.randint(0,len(list)-1)]

list = [7,8,9,34]
#print retrandom(list)

##Ques: Return n items in a list, selected at random, 
##      and if the same thing gets selected twice 
##      you reject it and try again.

def retnitems(list,n):
    s = []
    for i in range(n):
        temp = list[random.randint(0,len(list)-1)]
        if temp not in s:
            s.append(temp)
            i -= 1
    return s


list = [i for i in range(30)]
n = 3
print retnitems(list,n)
