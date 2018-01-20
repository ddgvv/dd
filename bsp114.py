#114th prb
n3,k3=map(int,input().split(' '))
l3=list(map(int,input().split(' ')))
s3=[]
for x in l3:
    if(x%2!=0):
        s3.append(x)
print(s3[k3-1])
