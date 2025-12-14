def BubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]> arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def flagbubblesort(arr):
    pass


def BubbleSortRec(arr):
    pass


arr = [15,22,2,55,4,9,16,24,67,103,9]
print(BubbleSort(arr))