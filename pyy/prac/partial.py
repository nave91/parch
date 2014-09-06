#Example of higher orderfunction

from functools import partial

def sum(x,y):
  return x+y

first = partial(sum,1)
print first,"first"
print first(2), "first(2)"
