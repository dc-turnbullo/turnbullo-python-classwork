print(ord("a"))

word = str(input())
arr = []
strarr = []
finalarr = []

for i in range(0,len(word)):
    arr.append(int(word[i])+96)
    finalarr.append(chr(arr[i]))

print(finalarr)
