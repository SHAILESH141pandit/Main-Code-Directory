# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.

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


class SmartPhone(Calculator2, Phone):
    print()
    print("SmartPhone Class")
    print()

obj = SmartPhone()
obj.multiplication(10 ,20)
obj.Division(30, 60)
obj.calling("VI", "4G", "Audio/Video")
obj.sms("Message2.0", "Text")