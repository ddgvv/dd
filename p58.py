sentence=input().split(' ')
w=input()
c=0
for i in sentence:
    if w == i:
        c+=1
print(c)
