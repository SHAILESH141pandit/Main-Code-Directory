# 8. Write a python script to implement try except and else block for division.

print("Enter two number: ")

try :
    n1, n2 = int(input(">>> ")), int(input(">>> "))
    print(n1/n2)

except ZeroDivisionError as err :
    print(err)
else :
    print("Not Zero Division Error")
