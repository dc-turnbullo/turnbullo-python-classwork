num = int(input())
n = int(input())

for i in range(0,n-1):
    num = num * 5
    while num % 10 == 0:
        num = num / 10

print(int(num))