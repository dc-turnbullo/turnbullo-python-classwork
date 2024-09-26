def sum_rows(matrix)
    row = []
    sums = []
    for i in range(0,len(matrix)):
        temptot = 0
        row = matrix[i]
        for j in range(0,len(row)):
            temptot = temptot + row[j]
        sums.append(temptot)
    return(sums)