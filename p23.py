n,k=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
k=list(input().split(' '))
m=[]
for i in range(len(k)):
    l.append(i)
    m.append(max(l))
    l.remove(i)
print(" ".join(str(x) for x in m))
