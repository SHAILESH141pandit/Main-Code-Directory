
class A:     
    def __init__(self):
        self.m1 = 9
 

class B(A): 
    
    def __init__(self):
        super().__init__()

        self.m2 = 8
    


obj = B()
# print(obj.m1)
print(obj.m2)
print(obj.m3)

  

   


