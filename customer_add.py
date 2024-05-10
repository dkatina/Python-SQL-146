from db_connection import connect_db, Error
from customer_fetch import fetch_all_customers

def add_customer():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is your name? ").title()
            email = input("What is your email? ")
            phone = input("Phone: ")

            new_customer = (name, email, phone)

            query = "INSERT INTO Customer (customer_name, email, phone) VALUES (%s, %s, %s)"

            cursor.execute(query, new_customer)
            conn.commit() #fully commits the changes
            print(f"New Customer {name} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()





