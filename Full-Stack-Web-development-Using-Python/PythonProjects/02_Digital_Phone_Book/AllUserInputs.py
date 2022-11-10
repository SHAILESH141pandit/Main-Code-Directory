def UserInput() :
    print()
    print("Enter User Details.")
    print()

    UserId = None
    while UserId == None :
        t = input("User Id    >>> ")
        if t.isdigit() and len(t)>=4 :
            UserId = t
        else :
            print("Invalied UserId. Please Enter only 4 or more digit number.")

    UserName = input("User Name  >>> ")

    Email = None
    while Email==None :
        t = input("Email      >>> ").lower()
        if t.endswith('@gmail.com') :
            Email = t
        else :
            print("Invalied Email.")
            
    Password = None
    while Password == None :
        t = input("Password   >>> ")
        if len(t)>=5 :
            Password = t
        else :
            print("Invalied Password. Please Enter only 5 or more Password.")

    myTuple = (UserId, UserName, Email, Password)
    return myTuple




def LoginInput() :
    Email = None
    print()
    while Email==None :
        t = input("Email       >>> ").lower()
        if t.endswith('@gmail.com') :
            Email = t
        else :
            print("Invalied Email.")
            
    Password = None
    while Password == None :
        t = input("Password    >>> ")
        if len(t)>=5 :
            Password = t
        else :
            print("Invalied Password. Please Enter only 5 or more Password.")

    return (Email,Password)
