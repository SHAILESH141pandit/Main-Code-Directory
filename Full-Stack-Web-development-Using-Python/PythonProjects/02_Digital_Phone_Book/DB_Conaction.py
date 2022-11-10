
import psycopg2
import psycopg2.extras
from PostGres_Details import *
from AllUserInputs import *



def UserResistationTable() :
    create_script = '''
                CREATE TABLE IF NOT EXISTS UserResistation(
                    User_Id int PRIMARY KEY,
                    User_Name varchar(20) NOT NULL,
                    Email varchar(30) NOT NULL,
                    Password varchar(50) NOT NULL
                    );'''
    return create_script



def UserContactTable() :
    create_script = '''
                CREATE TABLE IF NOT EXISTS UserContacts(
                    Contact_Id int PRIMARY KEY,
                    First_Name varchar(20) NOT NULL,
                    Last_Name varchar(20) NOT NULL,
                    Email varchar(30) NOT NULL,
                    Phone_Number int NOT NULL ,
                    User_Id int NOT NULL,
                    CONSTRAINT fk_UserResistation FOREIGN KEY(User_Id) REFERENCES UserResistation(User_Id)
                    );'''
    return create_script



def DB_Conection() :
    conn = None
    # User_Id = 100
    try :
        with psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id
                    ) as conn :
            with conn.cursor() as cur :
                
                cur.execute('DROP TABLE IF EXISTS employee')

                cur.execute(UserResistationTable())
                cur.execute(UserContactTable())
                
                while True :
                    print()
                    print("Do you want to Login or Registration. L for Login / R for Registration / Q for Quit!")
                    Yes_No = input("[L/R/Q]>>> ").lower()
                    if Yes_No=="r" :
                        cur.execute('SELECT * FROM UserResistation')
                        userRecord = UserInput()
                        for record in cur.fetchall() :
                            # print(record[0] , userRecord[0] , record[3] , userRecord[3])
                            if record[0] == userRecord[0] or record[3] == userRecord[3] :
                                print()
                                print('           >>> Please Login (If user is already registered)')
                            
                                # insert_script = 'INSERT INTO UserResistation(User_Id, User_Name, Email, Password) VALUES(%s, %s, %s, %s)'
                                # insert_value = (100, 'yash', 'yesh123@gmail.com', '12345')
                                # cur.execute(insert_script, insert_value)
                    
                    elif Yes_No=="l" :
                        print()
                        Un = LoginInput()
                        cur.execute('SELECT * FROM UserResistation')
                        for record in cur.fetchall() :
                            if record[2] == Un[0] and record[3]==Un[1] :
                                print("You are login")
                            print()
                            print('''
            [View]      > To view all saved contacts.
            [View -a]   > To view a specific saved contact.
            [Add]       > To Add a new contact.
            [Del]       > To Delete a contact.
            [Update]    > To Update an existing contact.
            [exit/quit] > To exit / quit the  program.
                            '''),print()
                            uIn = input("Command     >>> ")
                                
                    else :
                        break



    except Exception as error :
        print(error)
    finally :
        print("close")
        if conn is not None :
            conn.close()


DB_Conection()
# print(UserInput())

