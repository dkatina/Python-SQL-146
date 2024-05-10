from db_connection import connect_db, Error

def fetch_all_orders():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all orders
            query = "SELECT * FROM Orders;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()


def fetch_order(customer_id, order_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all orders
            query = "SELECT * FROM Orders WHERE customer_id = %s AND id = %s;"

            #Execute query
            cursor.execute(query, (customer_id, order_id))

            print(cursor.fetchall())
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()

