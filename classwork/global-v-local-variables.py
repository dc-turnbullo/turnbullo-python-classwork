import random
count = 0
num = 0
lowest = 1000000000
while lowest != 1:

    while num != 63:
        num = random.randint(0, 100)
        count +=1
    if count < lowest:
        lowest = count
    print("attempt total =", count)
print("number of runs needed to get 63 on first attempt =", lowest)
