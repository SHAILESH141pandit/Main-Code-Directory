
class A:     # 25 features

    def f1(self):
        print("In A f1")

class B(A):        # 27 features

    def f2(self):
        print("In B f2")

class C(B):

    def f3(self):
        print("in C f3")        



obj1 = C()
obj1.f1()
obj1.f2()
obj1.f3()