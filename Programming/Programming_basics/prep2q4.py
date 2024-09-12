print("enter one of the following options")
print("enter 'A' for multiply")
print("enter 'B' for divide")
print("enter 'C' for add")
print("enter 'D' for subtract")
print("enter 'E' for remainder (mod)")
selec = input()

if selec.lower() > "e":
    print("you have entered something outside the expected range >:( ")

selec = selec.lower()
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if selec == "a":
    print(num1 * num2)
elif selec == "b":
    print(num1 / num2)
elif selec == "c":
    print(num1 + num2)
elif selec == "d":
    print(num1/num2)
elif selec == "e":
    print(num1 % num2)

