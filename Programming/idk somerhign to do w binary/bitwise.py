def toUpper(string):
    result = ""
    mask = 0b01011111
    for character in string:
        ascii = ord(character)
        if ascii != 0b00100000:
            lc = ascii & mask
            result += chr(lc)
        else:
            result+= chr(ascii)
    
    print(result)
    return result

def toint(string):
    string = str(string)
    result = 0
    mask = 0b1111
    count = len(string)
    for character in string:
        print(f"character 1 is {character}")
        ascii = ord(character) - ord('0')
        num = ascii & mask
        result += num*10**(count-1)
        print(f"result of calculation {count} = {result}")
        count-=1
    print(result)
    return result


inp = str(input("enter a number"))
num = toint(inp)

