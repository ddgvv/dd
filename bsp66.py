def fact(v) :
    if v > 1:
        for i in range(2,v):
            if (v % i) == 0:
                return "no"
        return "yes"
    return "no"
v = int(input(
   "Enter value"))
print(fact(v))
