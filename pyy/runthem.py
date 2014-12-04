import os
import argparse

def neatprint(str):
    print "#"*50
    print str
    print "#"*50
            

if __name__=="__main__":
    
    
    onegoodsent = "Reads in dir as arg and executes all programs in it"
    parser = argparse.ArgumentParser(description=onegoodsent)

    parser.add_argument("idir",type=str,
                        help="input dir to load")

    a = parser.parse_args()
    
    if a.idir:
        idir = a.idir
    idir = './'+str(idir)
    programs = [ idir+'/'+i for i in os.listdir(idir)]
    for p in programs:
        with open(p,'r') as fp:
            neatprint("DISPLAYING: "+p)
            print fp.read()
            _ = raw_input()
            neatprint("EXECUTING: "+p)
            execfile(p)
            _ = raw_input()
