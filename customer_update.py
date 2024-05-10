from db_connection import connect_db, Error
from customer_fetch import fetch_all_customers

def update_customer_email(new_email, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            email_update = (new_email, customer_id)

            query = "UPDATE Customer SET email = %s WHERE id = %s;" #Update query 

            cursor.execute(query, email_update)
            conn.commit() #Make sure to commit on update
            print("Successfully Changed Email!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()



def update_customer_phone(new_phone, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            phone_update = (new_phone, customer_id)

            query = "UPDATE Customer SET phone = %s WHERE id = %s;" #Update query 

            cursor.execute(query, phone_update)
            conn.commit() #Make sure to commit on update
            print("Successfully Changed Phone!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()



def update_customer_name(new_name, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name_update = (new_name, customer_id)

            query = "UPDATE Customer SET customer_name = %s WHERE id = %s;" #Update query 

            cursor.execute(query, name_update)
            conn.commit() #Make sure to commit on update
            print("Successfully Changed name!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


