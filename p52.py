n,k=map(int,input().split(' '))
l=[]
for i in range(n):
    l.append(int(input()))
l=sorted(l)
print(l[k-1])
