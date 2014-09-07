"""
Implement a function with signature find_chars(string1, string2) 
that takes two strings and returns a string that 
contains only the characters found in string1 
and string two in the order that they are found in string1. 
Implement a version of order N*N and one of order N.
"""

def find_chars(str1,str2):
   out = ''
   for i in str1:
      for j in str2:
         if i==j: 
            if i not in out: out+=i
   print out

find_chars('nave','naveen')
