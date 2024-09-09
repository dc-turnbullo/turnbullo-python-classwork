time = int(input("enter minutes since midnight"))
hours = str(time // 60)
minutes = time % 60
if minutes <10:
    temp = str(minutes)
    minutes = "0" + temp
print(hours + ":" + minutes)