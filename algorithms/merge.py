def merge(arr1, arr2):
    i = 0
    j = 0
    arr3 = [None for _ in range(len(arr1) + len(arr2))]
    while True:
        if i >= len(arr2):
            finalarr = arr3[: i + j] + arr2[j:]
        if j >= len(arr1):
            finalarr = arr3 + arr1[i:]
            break
        else:
            if arr1[i] > arr2[j]:
                arr3[i + j] = arr2[j]
                j += 1
            else:
                arr3[i + j] = arr1[i]
                i += 1

    return finalarr


arr1 = [3, 4, 6, 7, 8, 12]
arr2 = [1, 5, 9, 13, 16, 17]

print(merge(arr1, arr2))
