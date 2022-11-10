from time import sleep
from threading import *

# Hello 
# Hi
# Main

class Hello(Thread):
    def run(self):
        for i in range(5):    
            print("Hello")
            sleep(2)



class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(2)


obj1 = Hello() # Hello thread created
obj2 = Hi() # Hi thread created

print("Welcome to the session")
print("We are learning threads")
x = 9

obj1.start() # Hello thread to start
sleep(1)
obj2.start()

obj1.join()
obj2.join()

print("Bye")

