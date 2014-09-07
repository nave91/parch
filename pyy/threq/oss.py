#OS fundamentals


import os

print os.getcwd(),"#"*5,"os.getcwd()"
print os.curdir,"#"*5,"os.curdir"
cd = os.curdir
print "cd = os.curdir"
cd = os.path.join(cd,"tools/wow")
print "cd = os.path.join(cd,'tools/wow')"
fil = os.path.join(cd,"fil.py")
print "fil = os.path.join(cd,'fil.py')"
print fil , "#"*5,"=fil"
print os.path.basename(fil),"#"*5,"os.path.basename(fil)"
print os.path.split(fil),"#"*5,"os.path.split(fil)"
print os.path.dirname(fil),"#"*5,"os.path.dirname(fil)"
print os.path.splitext(fil),"#"*5,"os.path.splitext(fil)"
print os.path.expanduser('~'),'#'*5,"print os.path.expanduser('~')"
