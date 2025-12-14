def insertionsort(arr, n):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def insertionsortrec(arr, n):



    if n <= 1:
        return arr


    insertionsortrec(arr, n - 1)

    # Insert the nth element into the sorted part
    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    return arr





arr = [15,22,2,55,4,9,16,24,67,103,9]
print(insertionsortrec(arr, len(arr)))