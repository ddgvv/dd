num,p=map(int,input().split(' '))
while(num%p==0):
    num/=p
if num==1:print('yes')
else: print('no')
