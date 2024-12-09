row = str(input("enter the things in the first row"))
lob = len(row)
counter = lob-1
triangle = []
def checkdiff(input1,input2):
    if (input1 == "r" or input2 == "r") and (input2 == "g" or input1 == "g"):
        return "b"
    elif input1 == (input1 == "r" or input2 == "r") and (input2 == "b" or input1 == "b"):
        return "g"
    else:
        return "r"


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
        print(triangle)
    counter -=1
print(triangle)