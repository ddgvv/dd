#66th problem
v = int(input("Enter value"))
if v > 1:
   for i in range(2,v):
       if (v % i) == 0:
           print("No")
           break
       else:print("Yes")
else:print("No")
