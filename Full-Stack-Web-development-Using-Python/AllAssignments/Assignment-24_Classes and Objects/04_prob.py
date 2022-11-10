# 4. Write a python program to init default values for user object using __init__ method.
class user:
    def __init__(self,var):
        self.var = var
        print(self.var)

obj = user("Hello")
