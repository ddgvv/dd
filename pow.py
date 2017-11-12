n=int(input())
c=0
while(n%2!=0):
    if n*(n-1)!=0 and (n-1)%2==0:
        n=n-1
        c=c+1
print(c)
    
