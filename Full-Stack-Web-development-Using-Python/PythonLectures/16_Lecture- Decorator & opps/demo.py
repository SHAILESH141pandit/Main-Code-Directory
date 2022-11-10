
# Object
# knows something - attributes
# does something - methods (functions)

class Computer:
    
    brand = "HP"    # class namespace

    def __init__(self, cpu, ram):
        self.cpu = cpu      # instance namespace
        self.ram = ram


    def show(self):
        print(self.cpu , self.ram)



com1 = Computer("i7", 8)
com2 = Computer("i9", 32)



com1.show() # Computer.show(com1,5) 

com2.show() #Computer.show(com2)


print(Computer.brand)

