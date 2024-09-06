complete = False
total = 0
nums = 0
while complete == False:
    num = int(input("Enter number to add, enter a negative to end program: "))
    if num >= 0:
        total = total + num
        nums = nums + 1
        total = total + 1
    else:
        complete = True

print(total / nums)
    
    