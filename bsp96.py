#96th prb
n = int(input("Enter any number : "))
if n> 1:
    for i in range(2, n):
        if (n % i) == 0:
            print("Yes")
            break
    else:
        print("No")
elif n == 0 or 1:
    print(" a neither prime NOR composite number")
else:
    print("Yes")
