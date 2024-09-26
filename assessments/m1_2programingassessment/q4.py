def find_largest_in_each_row(matrix):
    row = []
    maxs = []
    for i in range(0,len(matrix)):
        max = 0
        row = matrix[i]
        for j in range(0,len(matrix)):
            if row[j] > max:
                max = row[j]
            maxs.append(max)
    return maxs
