arr = []
num = 1
for i in range(0,64):
    arr.append(num)
    num = num * 2

count = 0
squares = int(input())
while squares >=0:
    squares = squares - arr[count]
    count += 1

if squares != 0:
    count -= 1

print(count)