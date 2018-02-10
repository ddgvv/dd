arr=list(map(int,input().split(' ')))
i=int(arr[1]**0.5)
if float(i)==float(arr[1]**0.5):
    if int(arr[1]**(0.5))==(arr[0]//4):print('yes')
    else:print('no')
else: print('no')
