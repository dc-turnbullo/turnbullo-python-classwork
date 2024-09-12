year = int(input("Enter a year: "))
leapyear = False
if (year % 4) == 0:
	leapyear = True

if (year % 100) == 0:
	leapyear = False

if  (year % 400) == 0:
	leapyear = True

if leapyear == True:
    print(year, "is a leapyear.")
else:
	print(year, "is not a leapyear.")