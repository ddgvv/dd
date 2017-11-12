l=input().strip().split(' ')
l=sorted(l)
l=l[::-1]
l="".join(str(x) for x in l)
l=l[::-1]
k=[]
for i in range(len(l)):
    if i%3==0 and i!=0:
        k.append(',')    
    k.append(l[i])
k=k[::-1]    
k="".join(str(x) for x in k)    
print(k)    
