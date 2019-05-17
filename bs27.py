v=input()
sum=0

for i in range(len(v)):
    sum+=int(v[i])**3
if v==str(sum): print("yes")
else:print("no")
