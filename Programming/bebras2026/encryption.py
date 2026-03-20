data = input()
originaldata = data

def encrypt(data):
    if len(data) %2 == 0:
        evencount = len(data) -2
    else:
        evencount = len(data) -2
    evenarr = []
    oddarr = []
    evenword = ""
    oddword = ""
    oddcount = 1
    while evencount >= 0 :
        evenarr.append(data[evencount])
        evencount -=2
    
    while oddcount <len(data):
        oddarr.append(data[oddcount])
        oddcount +=2
    for i in range(0,len(oddword)):
        oddword = f"{oddword}{oddarr[i]}"
    for i in range(0,len(evenword)):
        evenword = f"{evenword}{evenarr[i]}"
    
    encrypted = oddword + evenword
    return encrypted

counter = 0
newword = data
while True:
    newword = encrypt(newword)
    if newword == originaldata:
        break
    counter +=1

print(counter)
