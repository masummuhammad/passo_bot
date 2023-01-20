import sqlite3

connection=sqlite3.connect('DB1.db')

def initdb(email,password):
    
    cursor=connection.cursor()
    cursor.execute('drop table if exists header_data')


    cursor.execute('CREATE TABLE header_data(email text, token text ,refresh_token text ,password text)')
    cursor.execute("INSERT into 'header_data' VALUES('%s','abcd','efg','%s')"%(email,password))
    connection.commit()
    print("Database initialized.")
    

