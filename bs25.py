a,b=input("enter values").split(' ')
l = range(int(a)+1,int( b))
even= list(filter(lambda x: x%2==0, l))
print(" ".join(str(x) for x in even))
