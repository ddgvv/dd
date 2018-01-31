s1,s2=input().split(' ')
c=0
d=0
if(len(s1)==len(s2)):
    for i in range(0,len(s1)-1,1):
        if(s1[i]==s1[i+1]):
            c=c+1
            print(c)
        if(s2[i]==s2[i+1]):
            d=d+1
        if(c!=d):
            print('no')
            break
    print(c>0,c,d)
    if c==d:print('yes')
else:print('no')
