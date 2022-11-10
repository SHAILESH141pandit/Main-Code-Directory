# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the consol.

def reading(fileName):
    try:
        file = open(fileName,'r')
        text = file.read()
        print(text)
        file.close()

    except FileNotFoundError:
        print("File not found")

reading('Myfile.txt')
