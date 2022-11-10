'''
    7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
    hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
    values).
'''

class Laptop:
    brand, ram, cpu, hdd = 0, 0, 0, 0

    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print("Brand ",self.brand)
        print("Ram ",self.ram)
        print("Cpu ",self.cpu)
        print("Hdd ",self.hdd)

obj = Laptop("Apple", "4gb", "A5", "1TB")

obj.showConfig()