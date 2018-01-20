#87th prb
x1,y1=map(int,input().split(' '))
if x1 > y1:
    smaller = y1
else:
    smaller = x1
for i in range(1, smaller+1):
    if((x1 % i == 0) and (y1 % i == 0)):gcd1 = i
print(gcd1)
