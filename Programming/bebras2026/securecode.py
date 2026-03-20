code = input()
valid = True
if len(code) != 6:
    valid = False

try:
    num= int(code[0])

except:
    valid = False

try:
    num = int(code[5])
except:
    valid = False

for i in range(1,5):
    try:
        num= int(code[i])
        valid = False
    except:
        pass

if valid:
    print("valid")
else:
    print("invalid")