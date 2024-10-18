complete = False
total = 0
nums = 0
while complete == False:
    try:
        num = int(input("Enter number to add, enter a negative to end program: "))
    except:
        num = int(input("wrong type enter number to add negative to exit"))
    if num >= 0:
        total = total + num
        nums = nums + 1
        total = total + 1
    else:
        complete = True

print(total / nums)
    
    