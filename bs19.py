n,k=input("Enter n and k").split(' ')
n,k=int(n),int(k)
a=list(map(int,input("Enter values").split(' ')))
print(sum(a[:k]))
