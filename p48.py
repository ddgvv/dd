num=int(input())
arr=[]
for i in range(2, num):
    if num % i == 0 and i%2!=0:
        arr.append(i)
print(*arr)
