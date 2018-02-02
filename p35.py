ASCII = 256
def getMaxOccuringChar(s):
    count = [0] * ASCII
    m = -1
    c = ''
    for i in s:
        count[ord(i)]+=1;
    for i in s:
        if m < count[ord(i)]:
            m = count[ord(i)]
            c = i
    return c
s =input().split(' ')
print(" ".join(getMaxOccuringChar(k) for k in s))
