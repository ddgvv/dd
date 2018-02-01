lo,up=map(int,input().split(' '))
l=list(1 for i in range(up+1))
c=0
for i in range(2,up+1,1):
    if l[i]==1:
        for j in range(i*i,up+1,i):
            l[j]=0
        if i>=lo:
            c+=1
print(c)
