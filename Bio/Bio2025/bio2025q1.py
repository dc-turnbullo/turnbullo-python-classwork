#Oliver Turnbull, question 1 bio 2025
#Dulwich College


#101,111,202,222,303,333,404,444,505,555,606,616,626,636,646,656,666,676,686,696,707,717,727,737,747,757,767,777,808,888,909,999,1001,1111,2002,2112,2222,3003,3333,4004,4444,5005,5555
def invert3(sec):
    rightsec = sec[2] + sec[1] + sec[0]
    return rightsec

def invert2(sec):
    rightsec = sec[1] + sec[0]
    return rightsec

def test3(strnum):
    if strnum[0] == strnum[2]:
        return True
    else:
        return False

def test2(strnum):
    if strnum[0] == strnum[1]:
        return True
    else:
        return False
    



pns = [0,1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191,202,212,222,232,242,252,262,272,282,292,303,313,323,333,343,353,363,373,383,393,404,414,424,434,444,454,464,474,484,494,505,515,525,535,545,555,565,575,585,595,606,616,626,636,646,656,666,676,686,696,707,717,727,737,747,757,767,777,787,797,808,818,828,838,848,858,868,878,888,898,909,919,929,939,949,959,969,979,989,999,1001,1111,2002,2112,2222,3003,3333,4004,4444,5005,5555]

def checkpallindrome(num):
    strnum = str(num)
    midpoint = len(strnum)//2
    if len(strnum) == 3 and test3(strnum) == True:
        return True
    elif len(strnum) == 3:
        return False
    if len(strnum) == 2 and test2(strnum) == True:
        return True
    elif len(strnum) == 2:
        return False
    

    if len(strnum) == 1:
        return True
    
    leftsec = strnum[:midpoint]
    
    if len(leftsec) == 3:
        rightsec = invert3(leftsec)
    else:
        rightsec = invert2(leftsec)
    if len(strnum)%2 ==0:
        checkernum = leftsec + rightsec
    else:
        checkernum = leftsec + strnum[midpoint] + rightsec
    
    if checkernum == strnum:
        return True
    else:
        return False

def alterpns(pns,num):
    counter = 0
    while num < pns[counter]:
        counter+=1
    return pns[:counter]


def nextlowestpallindrome(num):
    strnum = str(num)
    midpoint = len(strnum)//2
    if len(strnum) == 3 and test3(strnum) == True:
        return True
    elif len(strnum) == 3:
        return False
    if len(strnum) == 2 and test2(strnum) == True:
        return True
    elif len(strnum) == 2:
        return False
    

    if len(strnum) == 1:
        return True
    
    leftsec = strnum[:midpoint]
    
    if len(leftsec) == 3:
        rightsec = invert3(leftsec)
    else:
        rightsec = invert2(leftsec)
    if len(strnum)%2 ==0:
        checkernum = leftsec + rightsec
    else:
        checkernum = leftsec + strnum[midpoint] + rightsec
    
    return checkernum

def pallindromeexceptionfixer(num):
    pass

palindromicfound = False

userinput = int(input("enter a number to find the palindromic something or others of"))
tempuserinput = userinput
alteredpns = alterpns(pns,userinput)
# for i in range(1,7):
#     try:
#         largepallindrome = int(nextlowestpallindrome(userinput))
#     except:
#         largepallindrome = int(nextlowestpallindrome(userinput - userinput//100))
#     for i in range(len(pns)):
#         for j in range(len(pns)):
#             if largepallindrome - pns[i]-pns[j] == 0:
#                 palindromicfound == True
#                 mediumpallindrome = pns[i]
#                 smallpallindrome = pns[j]

# print(largepallindrome)
# print(mediumpallindrome)
# print(smallpallindrome)

print(alteredpns)