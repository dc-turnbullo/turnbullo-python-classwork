def binarySearch(t, arr, lp, rp):
    while lp <= rp:
        mp = (rp + lp) // 2
        if arr[mp] == t:
            return mp
        elif t < arr[mp]:
            rp = mp -1
        else:
            lp = mp +1
    if arr[mp] == t:
        return mp
    else:
        return -1
    # endif
    # endwhile


# endprocedure


def binarySearchRec(t, arr, lp, rp):
    if lp > rp: 
        return -1

    mp = (lp + rp) // 2

    if arr[mp] == t:
        return mp
    elif t < arr[mp]:
        return binarySearchRec(t, arr, lp, mp - 1)
    else:
        return binarySearchRec(t, arr, mp + 1, rp)


array = [1, 5, 7, 12, 15, 22, 45]
lpt = 0
rpt = len(array) -1
print(binarySearchRec(15, array, lpt, rpt))
