print("1:Economy Car")
print("2: Saloon Car")
print("3: Sports Car")
checker = int(input())
if checker == 1:
    car = 1
    print("press 1 to proceed press 2 to cancel: ")
elif checker == 2:
    car = 2
    print("press 1 to proceed press 2 to cancel: ")
elif checker == 3:
    car = 3
    print("press 1 to proceed, press 2 to cancel: ")
else:
    print("invalid input")

if (int(input()) == 1) or (int(input()) == 2):
    print("have a nice day!")