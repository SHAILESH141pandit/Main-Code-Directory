# 05. Write a python script to handle multiple Exception in one try.
print("Enter two number: ")

try :
    num1 = int(input(': '))
    num2 = int(input(': '))
    print(num1/num2)
except ZeroDivisionError as error :
    print(error)
except ValueError as error :
    print(error)
except Exception as error :
    print(error)
