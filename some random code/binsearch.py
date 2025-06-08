def linearsearch(arr, findthingy):
    arrlen = len(arr)
    for i in range(0,arrlen):
        if arr[i] == findthingy:
            return i
    print("item not in array")
    return -1


def binarysearch(arr,findthingy):
    arr.sort()
    endpoint = len(arr) - 1
    startpoint = 0
    found = False
    while startpoint <= endpoint:
        midpoint = ((endpoint + startpoint)//2)
        if arr[midpoint] == findthingy:
            return midpoint
        elif findthingy < arr[midpoint]:
            endpoint = midpoint - 1
        elif findthingy > arr[midpoint]:
            startpoint = midpoint + 1
    return -1

def bubblesort(arr):
    arrlen = len(arr)
    swap = True
    while swap == True:
        swap = False
        count = 0
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swap = True
    print(arr)

def insertionsort(arr):
    sortedend = 1
    for j in range(sortedend,len(arr)):
        temp = arr[j]
        i = j -1
        while i >=0 and temp < arr[i]:
            arr[i+1] = arr[i]
            i-=1
            
        arr[i+1] = temp

    print(arr)
        


arr = []
while True:
    num = int(input("enter a number enter 0 to exit"))
    if num == 0:
        break
    arr.append(num)


def searcharr():
    output = binarysearch(arr,int(input("enter number to find")))

    if output == -1:
        print("not in array")
    else:
        print("item found in number", output + 1)

insertionsort(arr)