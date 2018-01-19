xx=int(input())
lx=[]
for i in range(1, xx + 1):
       if xx % i == 0:
           lx.append(i)
print(" ".join(str(n) for n in lx))
