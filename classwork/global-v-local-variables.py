import random
count = 0
num = 0
lowest = 1000000000
while lowest != 1:
    
    while num != 63:
        num = random.randint(0, 100)
        count +=1
    print("attempt total =", count)
    if count < lowest:
        lowest = count
    count = 0
        
print("number of runs needed to get 63 on first attempt =", lowest)
