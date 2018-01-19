import math
n2=int(input("Enter Value"))
if n2<10: print("10")
else:
    l2=len(str(n2))
    n2+=5
    n2=n2/(10**(l2-1))
    print(math.floor(n2)*(10**(l2-1)))
