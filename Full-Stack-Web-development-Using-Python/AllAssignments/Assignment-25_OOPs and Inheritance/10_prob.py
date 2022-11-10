'''
10. Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller.'''

class Calculator2:
    def multiplication(self, num1, num2):
        print("multiplication of two number is",num1*num2)
    def Division(self, num1, num2):
        print("Division of two number is",num1/num2)

class Phone:
    def calling(self, Service, Gen, callType):
        print("Service from",Service)
        print("Type",Gen)
        print("Call Type",callType)
    def sms(self, message, messageType):
        print("Message is :",message)
        print("Type of message is :",messageType)

class Truecaller:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def fetch(self):
        print("Name is: ",self.name)
        print("Number is: ",self.number)
        print()
    def TruecallerAdd_New_Entry(self, name, number):
        self.name = name
        self.number = number


class SmartPhone(Calculator2, Phone):
    def new_method(self, Truecaller_obj):
        Truecaller_obj.fetch()



obj = Truecaller("MySirG", 987456123)
phone = SmartPhone()
phone.new_method(obj)