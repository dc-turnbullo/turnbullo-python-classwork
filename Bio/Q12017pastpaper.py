row = str(input("enter the things in the first row"))
row = row.upper()
lob = len(row)
counter = lob-1
triangle = []
def checkdiff(input1,input2):
    input1 = input1.upper()
    input2 = input2.upper()
    if (input1 == "R" or input2 == "R") and (input2 == "G" or input1 == "G"):
        return "B"
    elif (input1 == "R" or input2 == "R") and (input2 == "B" or input1 == "B"):
        return "G"
    elif (input1 == "G" or input2 == "G") and (input2 == "B" or input1 == "B"):
        return "R"


for i in range(1,lob+1):
    triangle.append([""for j in range(i)])

for i in range(0,lob):
    triangle[lob-1][i] = row[i]


while counter >0:
    subcounter = 0
    while subcounter <counter:
        if triangle[counter][subcounter] == triangle[counter][subcounter+1]:
            triangle[counter-1][subcounter] = triangle[counter][subcounter]
        else:
            triangle[counter-1][subcounter] = checkdiff(triangle[counter][subcounter],triangle[counter][subcounter+1])
        subcounter+=1
    counter -=1
for i in range(lob):
    print(triangle[i])

print(triangle[0][0])