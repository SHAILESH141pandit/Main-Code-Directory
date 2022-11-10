# 7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).

class Phone:
    def calling(self, Service, Gen, callType):
        print("Service from",Service)
        print("Type",Gen)
        print("Call Type",callType)

    def sms(self, message, messageType):
        print("Message is :",message)
        print("Type of message is :",messageType)

features = Phone()

features.calling("Airtel", "4G", "Audio/Video")
features.sms("This is message.", "Text")