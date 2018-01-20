#81 problem
num=int(input("Enter the number of lines"))
for i in range(num):
    x,y=map(int,input("Ninja's and kabali's value").split(' '))
    print(abs(x-y))
