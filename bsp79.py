import math
ii,jj=map(int,input().split(' '))
n1=ii*jj
if math.sqrt(n1)==int( math.sqrt(n1)):
    print ("Yes")
else:
    print ("No")
