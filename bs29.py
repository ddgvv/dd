def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
num=int(input())
if num == 0:
   print("1")
else:
   print(fact(num))
