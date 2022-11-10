# 4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.

class Profile:
    name = 0
    email = 0
    age = 0
    plat_form = 0

    def __init__(self,plat_form):
        self.plat_form = plat_form
    
    def class_method(self):
        print(self.plat_form)

obj = Profile(25)

obj.class_method()
