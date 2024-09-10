conversion = 3.785
Carmileage = float(input("enter car mileage last time car was filled"))
Currentmileage = float(input("enter car mileage now"))
Totaltank = float(input("enter the number of liters taken to fill the tank"))


Mpg = (Currentmileage - Carmileage) / (Totaltank/conversion)
print(Mpg)