import mysql.connector #importing the mysql connector library that we pip installed
from mysql.connector import Error

def connect_db():
    db_name = "ecomm_db" #specifying
    user = "root" #selecting our user
    password = "BAC146" #grant access to db
    host = "127.0.0.1" #setting host localhost == 127.0.0.1

    #Establishing Connection
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print("Connected to MySQL Database")
            return conn # Returning our connection to be used elsewhere

    except Error as e:
        print(f"Error: {e}")
        return None
   

