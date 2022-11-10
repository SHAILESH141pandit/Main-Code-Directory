# def compare(s1,s2):
#     if s1.marks > s2.marks:
#         print("s1")
#     else:
#         print("s2") 

class Student:

    def __init__(self,marks):
        self.marks = marks
        
    def compare(self,other):
        if self.marks > other.marks:
            print("s1")
        else:
            print("s2") 


s1 = Student(25)
s2 = Student(20)



s1.compare(s2) # Student.compare(s1, s2)

# compare(s1, s2)

