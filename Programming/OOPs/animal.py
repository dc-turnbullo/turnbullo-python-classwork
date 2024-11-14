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
    def makenoise(self):
        print("Woof")



class Cat(animal):
    def makenoise(self):
        print("Meow")




myanimal = animal("unknown","oscar","yellow")
print(f"type: {myanimal.type} name: {myanimal.name} colour: {myanimal.colour}")
mydog = Dog("Dog","otto","white")
mycat = Cat("Cat","adam","brown")

mydog.makenoise()
mycat.makenoise()

animals = []
for animal in ["cat","dog","cat","dog","cat","dog","cat","dog"]:
    if animal == "cat":
        animals.append(Cat("Cat","unknown","unknown"))
    else:
        animals.append(Dog("Dog","unknown","unknown"))


for animal in animals:
    animal.makenoise()
