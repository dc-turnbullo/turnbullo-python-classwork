### SRC - Please make sure you are using the coding conventions, i.e. #end if
temp = int(input("enter temperature"))
humidity = int(input("enter humidity"))
window = input("is the window opened or closed? ")
if ((temp > 25) or (humidity > 50)) and (window == "closed"):
	print("open the window")
elif ((temp < 10) and (humidity < 50)) and (window == "open"):
	print("close the window")
else:
	print("everything is good!")
#end if
	
