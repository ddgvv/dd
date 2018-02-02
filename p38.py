val=int(input())
lis=[]
for i in range(2,val+1,2):
    if val%i==0:
        lis.append(i)
print(" ".join (str(i) for i in lis))
