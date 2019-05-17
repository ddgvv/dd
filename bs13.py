letter=input()
vowel=['a','e','i','o','u','A','E','I','O','U']
if not letter.isalpha():print('invalid')
elif letter in vowel: print("Vowel")
else: print("Consonant")
