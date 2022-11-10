# 04. Write a python script to handle a ValueError.

import math
num1 = -1
try:
    print(math.sqrt(num1))
except ValueError as error:
    print(error)