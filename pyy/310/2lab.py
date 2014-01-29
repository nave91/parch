#!/usr/bin/env python

##Python code for lab2##
##Ques: Return a dictionary, converted to a string, 
##      showing the keys and values (where the key,
##      value pairs are sorted descending by the
##      values).

dic={1:'one',2:'two',3:'three'}
for key in sorted(dic.keys(),reverse=True):
    print key,dic[key]
