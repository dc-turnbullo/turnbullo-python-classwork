#oops

class Dog:
    def __init__(self,myname,mycolour) -> None:
        self.name = myname
        self.colour = mycolour
    def bark(self,barktimes):
        for _ in range(barktimes):
            print("woof!")
    def setcolour(self,dogcolour):
        self.colour = dogcolour
    
    def getcolour(self):
        return self.colour

    #endprocedure
#endclass

mydog = Dog("fido","black")
mydog.bark(2)
print(mydog.name)
print(mydog.getcolour())
mydog.setcolour("brown")
print(mydog.getcolour())
mydog.bark(3)
        