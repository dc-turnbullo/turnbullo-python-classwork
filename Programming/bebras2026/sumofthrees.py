start = int(input())
end = int(input())
data = []
for i in range(start,end+1):
    data.append(i)

threes = []
for i in range(0,len(data)):
    if data[i] % 3 == 0:
        threes.append(data[i])
result = 0
for i in range(0,len(threes)):
    result += threes[i]

print(result)