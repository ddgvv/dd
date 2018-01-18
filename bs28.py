a,b=input().split()
a,b=int(a),int(b)
l=[]
for num in range(a+1,b):

   order = len(str(num))

   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       l.append(num)
print(" ".join(str(x) for x in l))
