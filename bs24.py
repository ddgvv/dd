a,b=input("enter values").split(' ')
l = range(int(a)+1,int( b))
odd = list(filter(lambda x: x%2==1, l))
print(" ".join(str(x) for x in odd))
