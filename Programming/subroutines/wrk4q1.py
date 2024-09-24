def multiples(table,startnum,endnum,pupilName):
    print("hi",pupilName,"... here is your timestable: ")
    for i in range(startnum,(endnum+1)):
        correct = False
        while correct == False:
            print(table, "x",i,"= ?")
            userinput = int(input())
            if userinput == i*table:
                print("Well done")
                correct = True
            else:
                print("wrong")
            #endif
        #endwhile
    #next i
#endprocedure




name = str(input("what is your name? "))
timestable = int(input("enter your timestable, start number and end number one at a time in that order or i will be sad :(  "))
startnumber = int(input())
endnumber = int(input())

multiples(timestable,startnumber,endnumber,name)