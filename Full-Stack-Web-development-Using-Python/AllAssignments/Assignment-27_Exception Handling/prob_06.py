# 06. Write a python script to create a calculator with 4 basic operations, and handle a maximum number of exceptions.
import math
def calculator(num1, num2) :
    print("""
    [+]     For Addition.
    [-]     For Subtraction.
    [*]     For multiplition
    [/]     For Division.
    [**]    For SubRoot.""")
    opr = input(">>> ")

    match opr :
        case "+":
            print("Addition is ",num1+num2)

        case "-" :
            print("Subtraction is ",num1-num2)

        case "*" :
            print("multiplition... is ",num1*num2)

        case "/" :
            print("division is ",num1/num2)

        case "**" :
            print(f"SubRoot number {num1} is ",math.sqrt(num1))
            print(f"SubRoot number {num2} is ",math.sqrt(num2))

print("Enter two number: ")

try :
    n1, n2 = int(input(">>> ")), int(input(">>> "))
    calculator(n1, n2)

except ZeroDivisionError as error :
    print(error)
except ValueError as error :
    print(error)
except TabError as error :
    print(error)
except Exception as error :
    print(error)