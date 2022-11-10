# 5. Write a Python script to append list of city names in a file ‘cities.txt’

def Append(FileName, cityName):
    file = open(FileName, 'a')
    file.write(cityName)
    file.close()

mylist = ['Patna', 'Bhopal', 'Delhi', 'Mumbai']
fileName = 'f1.txt'
for i in mylist :
    st = i + '\n'
    Append(fileName, st)

print("Complete!")

