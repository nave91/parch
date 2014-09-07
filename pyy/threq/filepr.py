#File processing

try: 
  with open("filepr.py",'rb') as f:
    print "#"*5+"printing file"+"#"*5
    print f.read()
except IOError:
  print "no file"
