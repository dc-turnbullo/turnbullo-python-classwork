arr = []
anotherarr = []
arr = input().split(",")

entered = 0
exited = 0
for i in range(0,len(arr)):
    anotherarr.append(arr[i].split(" "))



for i in range(0,len(anotherarr)):
    num = int(anotherarr[i][0])
    entered = entered + num
    num = int(anotherarr[i][1])
    exited = exited + num

print(entered - exited)
