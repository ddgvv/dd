#58th problem
a,b=map(int,input("Enter Two values").split(' '))
a = a ^ b;
b = a ^ b;
a = a ^ b;
print(a,b)
