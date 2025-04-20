sentence = input().replace(" ", "")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
missing = ''

for letter in alphabet:
    if letter not in sentence:
        missing += letter

print(missing)