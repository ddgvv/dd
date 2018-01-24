symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
def check(name):
    c=0
    for i in name:
        if i in symbol:
           c+=1
    return c           
print(check(input("Enter the String:")))
