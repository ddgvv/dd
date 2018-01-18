#38th prb
x,y = input().split(' ')
x,y=int(x),int(y)
x = x ^ y;
y = x ^ y;
x = x ^ y;
print(x,y)
