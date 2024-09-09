cont = True
total = 0
count = 0
while cont == True:
    num = int(input("enter a number, enter a negative num to stop entering"))
    if num < 0:
        cont = False
    else:
        total = total + num
        count = count + 1

print(total / count)
