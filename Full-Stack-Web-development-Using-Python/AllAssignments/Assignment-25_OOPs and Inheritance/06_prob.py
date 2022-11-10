# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.

class Calculator2:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiplication(self):
        print("multiplication of two number is",self.num1*self.num2)

    def Division(self):
        print("Division of two number is",self.num1/self.num2)

b = Calculator2(10, 20)

b.multiplication()
b.Division()