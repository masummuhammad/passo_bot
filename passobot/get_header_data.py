import sqlite3

from initdb import connection

cursor=connection.cursor()



def get_refresh_token_id(email):
    try:
            cursor.execute("select refresh_token from header_data where email ='%s';"%email)
            
            refresh_token_ = cursor.fetchone()
            return refresh_token_[0]
    except Exception as e:
        print(e)
        return "refresh_token not found"


def get_password(email):
    try:
        
        cursor.execute("select password from header_data where email='%s';"%(email))
        password=cursor.fetchone()
       
        return password[0]
        
    except Exception as e:
        print(e)
        return "password not found"


def get_token(email):
    try:
    
        cursor.execute("select token from header_data where email='%s';"%email)
        token=cursor.fetchone()
       
        return token[0]
    except Exception as e:
        print(e)
        return "get_token not found"


def get_phone_number(email):
    try:
        with connection.cursor() as cursor:
            sql = "select phone_number from header_data where email = '%s';"%email
            cursor.execute(sql)
            query_string_ = cursor.fetchone()
            return query_string_["phone_number"]
    except Exception as e:
        print(e)
        return "phone_number not found"








