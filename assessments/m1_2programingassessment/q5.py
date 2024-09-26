def matrix_diagonal_difference(matrix):
    row = 0
    column = 0
    pd = 0
    sd = 0
    for i in range(0,len(matrix)):
        pd = pd + matrix[row][column]
        row = row + 1
        column = column + 1
    column = 0
    for i in range(0,len(matrix)):
        sd = sd + matrix[row][column]
        row = row - 1
        column = column + 1
    difference = pd-sd
    return difference