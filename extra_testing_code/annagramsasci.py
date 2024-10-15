t = str(input("enterthingpakpowidjopiawjhdoihjaiowshjdiouhaqwoiudhjoilkajuosilkdfhjuisweDGTFUHIahsopilkuedfhiuop[QSHJUY EWFOIPDUHiaujoskpfhjd]"))
s = str(input("enter thingy"))
svalue = 0
tvalue = 0
temp = 0
if len(s) == len(t):
    for i in range(0,len(s)):
        temp = ord(s[i])
        svalue = svalue + int(temp)

    for i in range(0,len(t)):
        temp = ord(t[i])
        tvalue = tvalue + int(temp)

    if tvalue == svalue:
        print("true")
    else:
        print("false")
else:
    print("false")