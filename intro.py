import mysql.connector #importing the mysql connector library that we pip installed
from mysql.connector import Error

# Database connection Parameters
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

    cursor = conn.cursor() #Creating a cursor to act as the middle man between python and mysql

    query = "SELECT * FROM Customer;"

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    if conn.is_connected():
        print("Connected to MySQL Database")

except Error as e:
    print(f"Error: {e}")
finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close() #ALWAYS MAKE SURE YOU CLOSE YOUR CONNECTION WHEN DONE
        print("MySQL Connection Closed")

