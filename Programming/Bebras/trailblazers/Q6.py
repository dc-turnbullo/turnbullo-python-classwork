posts = 2
meters = 2
pickets = 8
railings = 2

arr = input().split(" ")
posts = int(arr[0])
railings = int(arr[1])
pickets = int(arr[2])
posts = posts - 2
railings = railings -2
pickets = pickets - 8


done = False

while done == False:
    posts = posts - 1
    pickets = pickets - 8
    railings = railings - 2
    if posts >=0 and pickets >=0 and railings >= 0:
        meters = meters + 2
    else:
        done = True


print(meters)
