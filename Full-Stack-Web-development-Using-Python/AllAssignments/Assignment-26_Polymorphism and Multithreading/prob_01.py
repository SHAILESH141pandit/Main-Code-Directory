# 1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.

class user:
    def multi(self, num1=1, num2=1, num3=1):
        solut = num1*num2*num3
        return solut

obj = user()

print(obj.multi())
print(obj.multi(2))
print(obj.multi(3, 3))
print(obj.multi(4, 4, 4))

