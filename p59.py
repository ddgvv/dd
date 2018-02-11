n=int(input())
l=''
for i in range(n):
    l+=input()
l=l[0:l.rindex('0')]
print(*list(x for x in l if x=='1'))
