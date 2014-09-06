#Example of assert

#Assert is used to check something

def inputeq10(inp):
  print "inside inp before assert"
  assert inp == 10
  print "inside inp after assert"

print "wow"
inputeq10(10)
inputeq10(15) #Gives assertionError

