n=int(input())
c=0
for a in range(n+1):
	for b in range(n+1):
		way=(a*1)+(b*2)
		if way==n:
			c+=1
print(c)
