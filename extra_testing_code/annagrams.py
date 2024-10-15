s = str(input("enter string"))
t = str(input("enter 2nd string"))
t_array = []
s_array = []
if len(s) == len(t):
    for i in range(0,len(s)):
        s_array.append(s[i])

    for i in range(0,len(t)):
        t_array.append(t[i])
    t_array = t_array.sort()
    s_array = s_array.sort()
    if t_array == s_array:
        print("true")
    else:
        print("false")
else:
    print("false")