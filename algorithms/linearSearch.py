def linearSearch(t, arr):
    for i in range(0,len(arr)):
        if arr[i] == t:
            return i
        #endif
    #next i
    return -1


def linearSearchRecursive(t, arr, i):
    if i == len(arr):
        return -1
    elif arr[i] == t:
        return(i)
    else:
        return linearSearchRecursive(t,arr, i+1)
    

array = [3,7,4,12,6,8]
uinp = int(input("enter number to search for"))
print(linearSearchRecursive(uinp,array,0))