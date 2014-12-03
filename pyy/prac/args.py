#Example explaining args of python


def sum(x,y,z):
  print x,"=x",y,"=y",z,"=z"
  return x+y+z

print sum(10,0,z=9)

lst = []
def s(*args,**kwargs):
  #global lst
  lst = args[0]
  print lst
  print kwargs


s([1,2,3],z={'a':'1','b':'2'})
print lst
