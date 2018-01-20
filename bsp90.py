#90th prb
l=list(input())
k1=[]
for x1 in l:
    if x1.isdigit():
        k1.append(x1)
print("".join(str(n) for n in k1))
