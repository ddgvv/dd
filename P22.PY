x,y=map(int,input("Enter two value").split(' '))
l=[]
for i in range(1,int(max([x,y])/2)+2,1):
    if x%i==0 and y%i==0:
        l.append(i)
if len(l)==1:print("1")
else:print(max(l))
