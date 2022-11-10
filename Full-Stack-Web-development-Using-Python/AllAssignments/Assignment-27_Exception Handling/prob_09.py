# 9. Write a python script to raise a ValueError.
import math
try:
    num1 = int(input("Enter a number: "))
    if num1 == str :
        raise ValueError("String are not allowed")
    print(math.sqrt(num1))

except ValueError as error:
    print(error)