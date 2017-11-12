def rotate(lst, x):
    return [lst[-x:] + lst[:-x]]
l=list(map(int,input().split(' ')))    
k=int(input())            
print(''.join(str(x) for x in rotate(l,k)))   
