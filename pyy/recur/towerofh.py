def movetower(height,frompole,topole,withpole):
    if height >=1:
        movetower(height-1,frompole,withpole,topole)
        movedisk(frompole,topole)
        movetower(height-1,withpole,topole,frompole)
def movedisk(frompole,topole):
    print "moved disk from "+frompole+" to "+topole

movetower(3,"A","B","C")
