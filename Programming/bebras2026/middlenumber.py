data = input().split()
c1 = False
for i in range(0,len(data)):
    data[i] = int(data[i])

midpoint = (len(data) + 1)/2
midpoint -= 1
if midpoint %1 == 0:
    midpoint = int(midpoint)
    c1 = True
    print(data[midpoint])
else:
    print(int((data[int(midpoint-0.5)] + data[int(midpoint+0.5)])/2))




