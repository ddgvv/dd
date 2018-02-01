p=int(input())
l=list(1 for i in range(p))
li=[]
for i in range(2,p,1):
    if l[i]==1:
        for j in range(i*i,p,i):
            l[j]=0
        if p%i==0:
            li.append(i)
print(" ".join(str(x) for x in li))
