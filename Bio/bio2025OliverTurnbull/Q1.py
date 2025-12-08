grid = [
    ["u","v","w","x","y"],
    ["p","q","r","s","t"],
    ["k","l","m","n","o"],
    ["f","g","h","i","j"],
    ["a","b","c","d","e"]
    ]

gridupright = [
    ["a","b","c","d","e"],
    ["f","g","h","i","j"],
    ["k","l","m","n","o"],
    ["p","q","r","s","t"],
    ["u","v","w","x","y"]
]

fives = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625]

userinput = str(input())
userinput = userinput.lower()

lenofgrid = fives[len(userinput)-1]

def getcoord(letter):
    for x in range(0,5):
        for y in range(0,5):
            if grid[x][y] == letter:
                return y,x

coords = []
for i in range(0,len(userinput)):
    coords.append(getcoord(userinput[i]))



x = 0
y = 0
for i in range(0,len(coords)):
    x += coords[i][0] * fives[len(coords)-i-1]
    y += coords[i][1] * fives[len(coords)-i-1]

x+=1
y+=1

print(f"{x} {y}")


