def leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0: return "yes"
            else: return "no"
        else: return "yes"
    else: return "no"


print(leap(int(input("Enter three number:"))))
