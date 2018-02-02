l1,l2,k=input().split(' ')
k=int(k)
c=0
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        c+=1
if c==k:print("yes")
else:print("no")
