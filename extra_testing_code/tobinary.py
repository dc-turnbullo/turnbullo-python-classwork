def tobinary(num):
    arr = []
    finalstring = ""
    while num > 0:
        if num % 2 == 0:
            arr.append("0")
        else:
            arr.append("1")
            num -=1
        num = num/2


    for i in range(1,len(arr) + 1):
        finalstring = finalstring + str(arr[i*-1])
    return finalstring

print(tobinary(int(input("enter a number: "))))
