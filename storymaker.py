
import sys
#giving commandline arguement
fn=sys.argv[1]
FH=open(fn,'w')
fl="created by story_maker.py"
FH.write(fl)
ll="copyright,<vinay>2019"
#importing seed and slice1 function
from window import seed,slice1
text=seed('alphabet.txt')
#giving commandline Arguement
lse=sys.argv[2]
val=slice1(int(lse))
FH.write(val)
FH.write(ll)
FH.close()
with open(fn)as RFH:
    a=RFH.read()
    print(a)



    
    
