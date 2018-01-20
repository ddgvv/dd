#85 problem
s=input("Enter a string")
list1=[]
list2=[]
for i in range(len(s)):
    if i%2==0:list1.append(s[i])
    else:list2.append(s[i])
print("".join(str(x) for x in list1),"".join(str(x) for x in list2))
