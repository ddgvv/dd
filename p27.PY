words=list(input())
for i in range(len(words )):
    if words[i].islower():
        words[i]=words[i].upper()
    else:
        words[i]=words[i].lower()
print(words)

#28 problem
words=input()
print(words.replace(" ",""))

