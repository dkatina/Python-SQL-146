from db_connection import connect_db, Error
from order_fetch import fetch_all_orders
from datetime import date

def add_order(date, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_order = (date, customer_id)

            query = "INSERT INTO Orders (order_date, customer_id) VALUES (%s, %s)"

            cursor.execute(query, new_order)
            conn.commit() #fully commits the changes
            print(f"New order added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


