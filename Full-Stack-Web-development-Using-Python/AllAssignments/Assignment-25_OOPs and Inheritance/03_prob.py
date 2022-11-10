# 3. Write a python script to update 2nd Question, change email and age to __email and __age.

class Profile:
    name = 0
    __email = 0
    __age = 0
    
obj = Profile()
obj.name = 'Yash'
obj.email = 'yash12345@gmail.com'
obj.age = 20

print(obj.name)
print(obj.email)
print(obj.age)