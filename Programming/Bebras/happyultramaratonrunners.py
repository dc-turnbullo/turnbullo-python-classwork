numberofrunners = int(input())

runers = [[] for j in range(0,numberofrunners)]

for i in range(0,numberofrunners):
    runers[i] = input().split(' ')
    for j in range(0,5):
        runers[i][j] = int(runers[i][j])


runerstemp = [_ for _ in runers]
happyruners = 0
for i in range(0,numberofrunners):
    runerstemp[i].sort()

for i in range(0,numberofrunners):
    if runers[i] == runerstemp[i]:
        happyruners +=1

print(happyruners)
print(runers)
print(runerstemp)