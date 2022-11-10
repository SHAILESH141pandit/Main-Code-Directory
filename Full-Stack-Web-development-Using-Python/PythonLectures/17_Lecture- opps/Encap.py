
# accesser and mutator
# getter and setter

# person -> firstname,lastname, phone, room no, city, state, marks1, marks2, marks3
# __age
# _age 
class Person:

    def __init__(self):
        self.__age = None
        self._name = "Navin"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age    


p1 = Person()
p1.set_age(19)

p1.college = "SSS"

p2 = Person()



# print(p1.__age)
print(p1._name)

#print(p1.get_age())

























