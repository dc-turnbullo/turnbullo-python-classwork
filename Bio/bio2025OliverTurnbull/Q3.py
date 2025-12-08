userinp = int(input())

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

        if tot > 1:
            return 0
    if tot == 0:
        return 0
    
    return 1



raindrops = 0
for i in range(start,userinp +1):
    raindrops += checkforraindrop(i)

print(raindrops)