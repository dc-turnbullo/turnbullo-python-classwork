arr1 = []
arr2 = []
print("enter 0 to mark last letter has been input letters in each arr have to be sorted already so like don't get up to anything funky w ur inputs buckaroonie")
while True:
    temp = str(input("enter a letter for arr 1:"))
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
count = 0
end = False
comp1 = False


while not end:
    if arr1[p1] < arr2[p2]:
        newarr.append(arr1[p1])
        p1 +=1
    else: 
        newarr.append(arr2[p2])
        p2 +=1

    #checking for p1 or p2 being end of arr
    if p1 == len(arr1):
        end = True
        comp1 = True
    
    if p2 == len(arr2):
        end = True
        comp1 = False


if comp1 == False:
    while p1 < len(arr1):
        newarr.append(arr1[p1])
        p1+=1
else:
    while p2 < len(arr2):
        newarr.append(arr2[p2])

print(newarr)