# 03. Write a python script to handle the ArithmeticError

num1 = 20
num2 = 0
try:
  arithmetic = num1/num2
  print(arithmetic)
except ArithmeticError as error:
  print(error)
  