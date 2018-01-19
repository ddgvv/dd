st=input()
if(len(st)%2==0):
    st=st[:int((len(st)/2))-1]+'**'+st[int(len(st)/2)+1:]
else:
    st=st[:int(len(st)/2)]+'*'+st[int(len(st)/2)+1:]
print(st)
