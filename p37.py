n=int(input("Enter the N value:"))
p1=[]
p2=[]
for x in range(n):
	l1=input()
	p1.append(l1)
for x in p1:
	for y in x:
		if y!=' ':
			p2.append(y)
print(min(p2))
