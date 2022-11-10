# 5. Write a python program to delete the age property of the user.

class user:
    age = 0
    def __init__(self, A):
        self.age = A
        print("Age :", self.age)
    def __del__(self):
        print("Destructor called, user deleted.")

Age = 45
obj = user(Age)
del obj
obj1 = user(36)