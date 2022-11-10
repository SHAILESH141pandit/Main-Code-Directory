# 5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.

class Calculator:

    def Add(self, num1, num2):
        print("Sum of two number is",num1+num2)

    def Subtract(self, num1, num2):
        print("Subtraction of two number is",num1-num2)

obj = Calculator()

obj.Add(10, 20)
obj.Subtract(40,30)