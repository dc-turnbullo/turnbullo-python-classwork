n = int(input())
small = 0
large = 0
large = n//24
remainder = n%24
if remainder %5 == 0:
    small = remainder // 5
else:
    small = remainder // 5
    small = small + 1

print(large,small)

