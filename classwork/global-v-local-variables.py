import random


def makerandomnum():
    num = 0
    count = 0
    while num != 63:
        num = random.randint(0, 100)
        count +=1
    return count



count = 0
num = 0
lowest = 1000000000
while lowest != 1:
    
    numattemptsto63 = makerandomnum()
    print("attempt total =", numattemptsto63)
    if numattemptsto63 < lowest:
        lowest = numattemptsto63
    
        
print("number of runs needed to get 63 on first attempt =", lowest)
