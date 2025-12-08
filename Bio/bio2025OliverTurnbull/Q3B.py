userinp = int(input("enter a number"))

strinp = str(userinp)
start = 10

def comparedigits(a,b):
    c = int(a)
    d = int(b)
    if c > d:
        return 1
    else:
        return 0

def checkforraindrop(num):
    strnum = str(num)
    tot = 0
    for i in range(0,len(strnum) -1):
        tot += comparedigits(strnum[i],strnum[i+1])
        if tot >1:
            return 0
    if tot == 0:
        return 0
    return 1

complete = False
counter = 0
tot = 0
while not complete:
    tot += checkforraindrop(counter+start)
    counter +=1
    if tot % 100000 == 0:
        print("100000 done")
    if tot == 10000000000:
        complete = True
        print(counter+start)
    

    

