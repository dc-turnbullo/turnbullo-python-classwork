hours = int(input("enter Hour: "))
minutes = int(input("enter Minute: "))
daytime = str(input("enter Daytime am or pm: "))
if hours == 12:
    hours = 0

minutes = minutes + hours * 60

if daytime == "pm" :
    minutes = minutes + (12 * 60)

print(minutes)