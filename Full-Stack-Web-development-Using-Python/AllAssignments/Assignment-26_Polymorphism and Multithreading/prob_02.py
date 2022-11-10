'''
    2. Write a python script to create a user account class with 2 instance variables (userid
    and balance). Create 3 user objects and add all the users using operator overloading.
'''
class userAccount:
    def user(self, userid=None, balance=None) :
        if userid != None and balance != None :
            self.userid = userid
            self.balance = balance

        elif balance != None :
            self.balance = balance

        elif balance == None :
            self.userid = userid
            # self.balance = balance

obj1 = userAccount()
obj2 = userAccount()
obj3 = userAccount()

obj1.user("D1")
print("Userid1 :",obj1.userid)
obj1.user(balance = 1200)
print("Balance :",obj1.balance)

obj2.user("E1")
print("Userid2 :",obj2.userid)
obj2.user(balance = 1300)
print("Balance :",obj2.balance)


obj3.user("F1")
print("Userid3 :",obj3.userid)
obj3.user(balance = 1400)
print("Balance :",obj3.balance)
