def partdigitvalidate():
    while True:
        part = input("enter valid 4 digit part code: ")
        if len(part) > 4 or len(part) < 4:
            print("invalid part code")
        else:
            break
    return(part)

oldcodes = 0
codes = 0
partcode = partdigitvalidate()
while partcode != "9999":
    if (int(partcode[-1]) >=6) and (int(partcode[-1]) <= 8):
        oldcodes = oldcodes + 1
    codes = codes + 1
    partcode = partdigitvalidate()

print("there are",oldcodes,"old codes and",codes,"total codes")