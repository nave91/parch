#example optional args

def mutliarg(arg1,*one,**many):
  print arg1,one,many


print "mutliarg('some',1,2,3,name=3)",
print 
mutliarg("some",1,2,3,name=3)  

