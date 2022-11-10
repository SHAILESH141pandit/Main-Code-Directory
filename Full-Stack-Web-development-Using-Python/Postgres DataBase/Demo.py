
import psycopg2
import psycopg2.extras

class DB_Conection :

    def Add(self, AddQuerry) :
        obj = DB_Conection()
        obj.DB_Conection(Add=AddQuerry)

    def Viewall(self, ViewallQuerry) :
        # obj = DB_Conection()
        obj.DB_Conection(Viewall=ViewallQuerry)





    def DB_Conection(self, create_script=None, Add=None, View=None, Viewall=None, delete=None, update=None) :

        hostname = 'localhost'
        database =  'PythonDB'
        username = 'postgres'
        pwd = 'test125'
        port_id = '5432'

        conn = None

        try :
            with psycopg2.connect(
                        host = hostname,
                        dbname = database,
                        user = username,
                        password = pwd,
                        port = port_id
                        ) as conn :
                with conn.cursor() as cur :
                
                    # cur.execute('DROP TABLE IF EXISTS employee')





                    #Quarry----------------Quarry-------------------Quarry------------------------- Quarry
                    
                    if Add!=None :
                        print("ADD")
                        insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES(%s, %s, %s, %s)'
                        cur.execute(insert_script, Add)

                    elif View!=None :
                        cur.execute(View)

                    elif Viewall!=None :
                        cur.execute(f'SELECT * FROM {Viewall}')
                        for record in cur.fetchall() :
                            for i in range(len(record)) :
                                print(record[i],end=' ')
                            print(end='\n')
                        
                    
                    elif delete!=None :
                        cur.execute(delete)
                    
                    elif update!=None :
                        cur.execute(update)

                    #Quarry----------------Quarry-------------------Quarry------------------------- Quarry






        except Exception as error :
            print(error)
        finally :
            if conn is not None :
                conn.close()



insert_value = (9, 'Aashok', 8000, 'D8')
obj = DB_Conection()
obj.Add(insert_value)
obj.Viewall('employee')

print("End")

