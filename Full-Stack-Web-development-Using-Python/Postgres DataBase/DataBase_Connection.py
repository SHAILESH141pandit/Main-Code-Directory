import psycopg2

hostname = 'localhost'
database =  'PythonDB'
username = 'postgres'
pwd = 'test125'
port_id = '5432'

conn, cur = None, None

try :
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
                )
    cur = conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS employee')




    create_script = '''
                CREATE TABLE IF NOT EXISTS employee(
                    id int PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    salary int,
                    dept_id varchar(50)
                    )'''
    cur.execute(create_script)





    insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES(%s, %s, %s, %s)'
    insert_value = (1, 'yash', 12000, 'D1')

    cur.execute(insert_script, insert_value)

    insert_values = [(2, 'mohit', 1500, 'D2'), (3, 'raju', 2000, 'D1'), (4, 'alok', 8000, 'D4'), (5, 'amit', 5000, 'D3')]
    
    for record in insert_values :
        cur.execute(insert_script, record)

    cur.execute('SELECT * FROM employee')
    # print(cur.fetchall())

    for record in cur.fetchall() :
        # print(record)
        print(record[1], record[2])





    conn.commit()
except Exception as error :
    print(error)
finally :
    if cur is not None :
        cur.close()
    if conn is not None :
        conn.close()
