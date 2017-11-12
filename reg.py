l=list(map(int,input().split(' ')))
k=[]
for i in l:
    if(l.count(i)>1):
        if(i not in k):
            k.append(i)
            print(i)
