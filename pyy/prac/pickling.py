import pickle

a = ['wow','oh wow','wow wow wow']

fname = "picklefile"
f = open(fname,'wb')

pickle.dump(a,f)

f.close()

import os
os.system("cat "+fname)

f = open(fname,'rb')

b = pickle.load(f)

print a,b
