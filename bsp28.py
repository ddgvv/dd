#28th prb
n=int(input("Enter the size"))
l=list(map(int,input("Enter the values").split(' ')))
for x in l:
    print(x,l.index(x))
