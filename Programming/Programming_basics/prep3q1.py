max = ""
min = "z"
word = str(input("enter a 5 letter lowercase set of characters"))
for i in range(0,5):
    if word[i] > max:
        max = word[i]
    elif word[i]<min:
        min = word[i]


print(min)
print(max)