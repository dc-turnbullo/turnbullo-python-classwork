swimmers = input().split(" ")
for i in range(0,len(swimmers)):
    swimmers[i] = int(swimmers[i])
indexer = 0
maxi = len(swimmers)
done = False
count = 1
final = "1 "
while done == False:
    next = False
    count += 1
    fastest = swimmers[indexer]
    boundaries = fastest + 10
    indexer +=1 
    while next == False:
        if indexer >= maxi: 
            done = True
            break
        if swimmers[indexer + 1] < boundaries:
            final= final + str(count)
            final = final + " "
            indexer += 1
        else:
            next = True

print(final)
        