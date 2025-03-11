def validiprange(ipsegment):
    ipseg = int(ipsegment)
    if ipseg >=0 and ipseg < 256:
        return True
    return False

flag = False
iparr = input().split(".")
if len(iparr) != 4:
    flag = False
elif validiprange(iparr[0]) and validiprange(iparr[1]) and validiprange(iparr[2]) and validiprange(iparr[3]):
    flag = True


if flag == True:
    print("Valid IP Address")
else:
    print("Invalid IP Address")