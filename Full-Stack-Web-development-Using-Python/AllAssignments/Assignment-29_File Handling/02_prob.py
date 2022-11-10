# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

def Writing(text):
    file = open('Myfile.txt', "w")
    file.write(text)
    file.close()

tx = input("Enter some text: ")
Writing(tx)
