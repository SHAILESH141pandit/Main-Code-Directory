'''
9. Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).'''

class Truecaller:

    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def fetch(self):
        print("Name is: ",self.name)
        print("Number is: ",self.number)
        print()

    def TruecallerAdd_New_Entry(self, name, number):
        self.name = name
        self.number = number

obj = Truecaller("MySirG", 987456123)

obj.fetch()

obj.TruecallerAdd_New_Entry("New Entry 1", 12345)
obj.fetch()

obj.TruecallerAdd_New_Entry("New Entry 2", 98765)
obj.fetch()