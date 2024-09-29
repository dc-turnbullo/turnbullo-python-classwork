def addnames(names):
    userinput = str(input("enter name"))
    names.append(userinput)
    return names
#endfunction

def displaylist(names):
        print(names)
    #next i
#endfunction

def displaymenu():
    print("1 addname")
    print("2 display list")
    print("3 quit")
#endfunction
while True:
    name = 0
    names = []
    correct = False
    displaymenu()
    while True:
        decision = int(input("enter your choice: "))
        if (decision > 0) and (decision<4):
            correct = True
            break
        else:
            print("invalid choice please enter again: ")
        #endif
    #endwhile
    if decision == 3:
        print("program terminating")
        break
    elif decision == 2:
        displaylist(names)
    else:
        names = addnames(names)
    #endif
#endwhile/program
