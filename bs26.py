a,b=input().split(' ')
a,b=int(a),int(b)
l=[]
for num in range(a+1,b):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           l.append(num)
print(" ".join(str(xz) for xz in l))
