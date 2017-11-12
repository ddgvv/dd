
l=input()
K=int(input())
l=sorted(l)
l="".join(str(x) for x in l)
print(l[:len(l)-K])
