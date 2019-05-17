s1,s2=input().split(' ')
c=0
l=len(s1)
for i in range(l):
    if s1[i]!=s2[i]:
        c=c+1
if(c==1):print('yes')
else:print('no')
