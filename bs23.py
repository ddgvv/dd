def prime(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:return "no"
            else: return "yes"
    else:return "no"
print(prime(int(input("Enter the Number"))))
