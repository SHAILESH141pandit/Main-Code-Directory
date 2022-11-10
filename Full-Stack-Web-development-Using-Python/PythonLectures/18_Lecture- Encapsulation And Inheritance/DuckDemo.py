

# Duck Typing



class VSCode:

    def execute(self):
        print("Compile")
        print("Run")


class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compile")
        print("Run")

class Notepad:

    def show():
        print("showing")

class Laptop:

    def code(self,ide):
        print("Coding..")
        ide.execute()


lap1 = Laptop()
ide = Notepad()

lap1.code(ide)


#  IDE -> Integrated Development Environment
