import random
#Oliver Turnbull, Dulwich college
numfuses = int(input("enter number of fuses"))
fuses = []
for i in range(0, numfuses):
    fuse = int(input("enter the time of fuse"))
    fuses.append(fuse)


fusetimers = []
if numfuses >= 1:
    fuse1time = [fuses[0]/2,fuses[0]]
    fusetimers.append(fuse1time)
if numfuses >= 2:
    fuse2time = [fuses[1]/2,fuses[0]]
    fusetimers.append(fuse2time)
if numfuses >=3:
    fuse3time = [fuses[2]/2,fuses[2]]
    fusetimers.append(fuse3time)
if numfuses >=4:
    fuse4time = [fuses[3]/2,fuses[3]]
    fusetimers.append(fuse4time)

totaltimes = []
for j in range(0,len(fusetimers)):
    for i in range(0,len(fusetimers)):
        totaltimes.append(fusetimers[i][0] +  fusetimers[j][0])
        totaltimes.append(fusetimers[i][1] + fusetimers[j][0])
        totaltimes.append(fusetimers[i][0] +  fusetimers[j][1])
        totaltimes.append(fusetimers[i][1] + fusetimers[j][1])
print(totaltimes)
totaltimes.sort()
print(totaltimes)
for i in range(0, len(totaltimes) -1):
    if totaltimes[i+1] == totaltimes[i]:
        totaltimes[i] = 1000000000000000000000000
count = 0
totaltimes.sort()
while totaltimes[count] < 1000000:
    count +=1

print(count *2 + 1)
print("oliver turnbull, Dulwich college")


