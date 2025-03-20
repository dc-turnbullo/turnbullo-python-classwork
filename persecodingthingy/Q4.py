square = int(input())
row = [[int(input())]for _ in range(0,square-1)]
column = []
coltot = 0
for rows in range(0,square-1):
    for col in range(0,square):
        coltot = coltot + row[rows][col]
    column.append(coltot)
    coltot = 0

print(column)
