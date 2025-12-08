print("BD")
def encryption(arr, c, s):
    for i in range(0,s):
        mp = len(arr)//2
        alpha = arr[:mp]
        beta = arr[mp:]
        combined1 = []
        for i in range(0,len(alpha)):
            combined1.append(beta[i])
            combined1.append(alpha[i])
        for i in range(0,c):
            temp = combined1[0]
            combined1 = combined1[1:]
            combined1.append(temp)
        arr = combined1
    return arr

def isitin(z,alpha):
    for i in range(0,len(alpha)):
        if alpha[i] == z:
            return 1
    return 0

def makedecks(arr,alphabet):
    complete = False
    count = 0
    pre = arr
    alpha = []
    beta = []
    while not complete:
        temp = pre[count]
        if isitin(temp,alpha) == 1:
            beta.append(temp)
        else:
            alpha.append(temp)

        count+=1
        if count>= len(arr):
            complete = True
    return alpha, beta

def flipthrough(a,b,t):
    complete = False
    while not complete:
        if a[0] != t:
            temp = a[0]
            a1 = a[1:]
            a1.append(temp)
            a = a1
            temp = b[0]
            b1 = b[1:]
            b1.append(temp)
            b = b1
        else:
            return b[0]
        

def furtherencrypt(alpha,beta):
    pass

userinput = str(input("enter a string"))
partialinput = userinput.split()
n1 = int(partialinput[0])
s1 = int(partialinput[1])
c1 = int(partialinput[2])
stringinp = partialinput[3]
initialarray = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]

initialarray = initialarray[:(n1*2)]
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
array = encryption(initialarray,c1,s1)
alpha,beta = makedecks(array,alphabet)
#print(flipthrough(alpha,beta,stringinp[0]))
print("BD")