class stack:
    def __init__(self,maxsize):
        self.size = maxsize
        self.stack = [None for _ in range(maxsize)]
        self.sp = -1
    
    def p0p(self): 
        if self.isempty():
            print("Stack is empty you cannot pop from stack.")
        else:
            temp = self.stack[self.sp]
            self.stack[self.sp] = None
            self.sp -=1
            print("value removed from stack: "+  temp)
            return temp
    
    def isempty(self):
        if self.sp < 0:
            return True
        else:
            return False
        
    def isfull(self):
        if self.sp == self.size -1:
            return True
        else:
            return False
    
    def push(self,input):
        if self.isfull():
            print("stack is full, cannot push to stack")
        else:
            self.sp += 1
            self.stack[self.sp] = input
            print("push successful")

    def peek(self):
        print("value on the top of the stack is: "+ self.stack[self.sp])
    
    def __repr__(self):
        
        return self.stack



st1 = stack(10)


while True:
    usri = str(input("enter a command and then the nesecary parameters separated by a space, enter -- to exit"))
    if usri == "--":
        print("exiting stack, see you again soon :)")
        break
    
    space = usri.find(" ")

    
    if usri == "pop":
        st1.p0p()
    elif usri[:space] == "push":
        st1.push(usri[space + 1:])
    elif usri == "peek":
        st1.peek()
    elif usri == "print":
        print(st1.__repr__)