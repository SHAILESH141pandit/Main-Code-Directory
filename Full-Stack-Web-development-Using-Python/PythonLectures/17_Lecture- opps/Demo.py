
# Types of methods
# Encapsulation
# Inheritance

class Student:

    school = "Ineuron"          # class variable

    def __init__(self):
        self.marks = 10

    def get_marks(self):            # instance methods
        return self.marks

    @classmethod
    def get_school(cls):            # class methods
        return cls.school

    @staticmethod
    def add(x,y):                   # static methods
        return x+y    


s1 = Student()
s2 = Student()

print(s1.get_marks())
print(s1.marks)
print(Student.get_school())
print(s1.add(3,5))


