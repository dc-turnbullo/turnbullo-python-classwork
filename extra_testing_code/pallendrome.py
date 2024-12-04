def flip_string(string):
    pass


while True:
    num = str(input("enter number up to 20 digits"))
    if len(num) <= 20:
        break

mid = len(num) // 2
firsthalf = num[:mid]
print(firsthalf)
print(num[mid])
firsthalf = firsthalf + firsthalf[-1]
print(firsthalf)