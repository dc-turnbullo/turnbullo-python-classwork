arr1 = []
arr2 = []
print("enter 0 to say last letter has been input. letters in each arr have to be sorted already")
while True:
    temp = str(input("enter a letter for arr 1: "))
    if temp == "0":
        break
    else:
        arr1.append(temp)

while True:
    temp = str(input("enter a letter for arr 2: "))
    if temp == "0":
        break
    else:
        arr2.append(temp)

p1 = 0
p2 = 0
newarr = []

while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] < arr2[p2]:
        newarr.append(arr1[p1])
        p1 += 1
    else: 
        newarr.append(arr2[p2])
        p2 += 1


while p1 < len(arr1):
    newarr.append(arr1[p1])
    p1 += 1

while p2 < len(arr2):
    newarr.append(arr2[p2])
    p2 += 1

print("Merged array:", newarr)