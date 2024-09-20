def multiply(a: int,b: int): # parameters are in the brackets. 
# ": int" tells the subroutine that it should be an integer
    print("the product is",a*b)
    return
#end procedure


#main
first = int(input("enter first integer"))
second = int(input("Enter second integer"))
multiply(first,second) # arguments are in brackets
