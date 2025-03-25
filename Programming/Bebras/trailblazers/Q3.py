n = int(input())
sequence = input().split(" ")
missing = 0
for i in range(0,len(sequence)):
    sequence[i] = int(sequence[i])

if sequence[-1] != n:
    missing = n
elif sequence[0] != 1:
    missing = 1
else:

    for i in range(0,len(sequence)-1):
        if sequence[i+1] - sequence[1] != 1:
            missing = sequence[i] + 1

print(missing)
