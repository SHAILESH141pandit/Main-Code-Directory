# 4. Write a Python script to store a list of city names in a file ‘cities.txt’

def Scity(cityName):
    file = open('cities.txt', 'a')
    file.write(cityName)
    file.close()

mylist = ['Patna', 'Bhopal', 'Delhi']

for i in mylist :
    st = i + '\n'
    Scity(st)

print("Complete")
