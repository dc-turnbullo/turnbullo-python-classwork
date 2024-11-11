class animal:
    def __init__(self,type,name,colour):
        self.type = type
        self.name = name
        self.colour = colour
    #end constructor


    def makenoise(self):
        pass

    def move(self):
        pass

    def eat(self):
        pass
#endofclass

class Dog(animal):
    pass

myanimal = animal("unknown","adam","yellow")
print(f"type: {myanimal.type} name: {myanimal.name} colour: {myanimal.colour}")