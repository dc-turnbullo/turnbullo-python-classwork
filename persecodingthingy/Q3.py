intwave = int(input())
strwave = str(intwave)
numflats = len(strwave) // 2
waveamps = []
waveflats = []
count = 0
for i in range(0,numflats):
    waveamps.append(strwave[count])
    count +=2

count = 1
for i in range(0,numflats):
    waveflats.append(strwave[count])
    count+=2

wavelength = 0
for i in range(0,len(waveflats)):
    wavelength += int(waveflats[i])

print(wavelength)
waveimage = [["."for i in range(0,wavelength)]for j in range(0,10)]


count = 0
while count < wavelength:
    for i in range(0,waveflats[i]):
        waveimage[waveamps[i]][i] = "@"

