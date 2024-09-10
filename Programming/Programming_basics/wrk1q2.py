Width = float(input("enter width of room: "))
length = float(input("enter the length of the room: "))
height = float(input("enter the height of the room: "))
unprint = int(input("enter the number of unpaintable areas there are: "))

uArea = 0
for i in range(1,unprint + 1):
    uwidth = float(input("enter the width of the unpaintable area: " ))
    ulength = float(input("enter the length of the unpaintable area: " ))
    uArea = uArea + (uwidth * ulength)
#next i


area = Width * length
area = area - uArea
area = area + (Width * height * 2)
area = area + (length * height * 2)

paint = area / 11

print("you need", paint, "litres of paint")