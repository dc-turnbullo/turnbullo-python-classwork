def binarySearch(t, arr, lp, rp):
    while rp != lp:
        mp = (rp - lp) // 2
        if arr[mp] == t:
            return mp
        elif t < arr[mp]:
            rp = mp
        else:
            lp = mp
    if arr[mp] == t:
        return mp
    else:
        return -1
    # endif
    # endwhile


# endprocedure


def binarySearchRec(t, arr, lp, rp):
    mp = (rp - lp) // 2
    if rp == lp:
        return -1
    elif arr[mp] == t:
        return mp
    else:
        if t < arr[mp]:
            rp = mp - 1
            return binarySearchRec(t, arr[: (mp - 1)], lp, rp)
        else:
            lp = mp + 1
            return binarySearchRec(t, arr[(mp + 1) :], lp, rp)


array = [1, 5, 7, 12, 15, 22, 45]
lpt = 0
rpt = len(array)
print(binarySearch(7, array, lpt, rpt))
