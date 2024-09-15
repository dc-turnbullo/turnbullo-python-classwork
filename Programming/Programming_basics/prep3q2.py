password = "Tues1212"
count = 0
cont = True
while (count < 3) and (cont == True):
    attempt = str(input("enter password: "))
    if attempt == password:
        cont = False
        print("password accepted")
    else:
        count = count + 1
        print("wrong password!")


if count == 3:
    print("password rejected")