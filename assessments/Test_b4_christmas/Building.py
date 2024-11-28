class Building:
    def __init__(self,pheight,pwidth,pfloors) -> None:
        self.__height = pheight 
        self.__width = pwidth
        self.__floors = pfloors
    
    def getnumberoffloors(self):
        return self.__floors()
    
    def setnumberoffloors(self,pfloors):
        if pfloors >=1:
            self.__floors = pfloors
            return True
        else:
            return False



class House(Building):
    def __init__(self,pbedrooms,pbathrooms,pheight,pwidth,pfloors) -> None:
        super.__init__(pheight,pwidth,pfloors)
        self.bathrooms = pbathrooms
        self.bedrooms = pbedrooms


myhome = House(3,2,6,4,2)