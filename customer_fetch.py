from db_connection import connect_db, Error

def fetch_all_customers():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all customers
            query = "SELECT * FROM Customer;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) {row[1]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()


def fetch_customer():
    conn = connect_db()
    if conn is not None:
        try:
            customer_id = int(input("What is the id of the customer you're lookin for?"))
            cursor = conn.cursor()

            query = 'SELECT * FROM Customer WHERE id = %s'

            cursor.execute(query, (customer_id,))

            row = cursor.fetchall()[0]
            print(f"{row[0]}.) {row[1]}'s Contact info Email: {row[2]} Phone: {row[3]}.")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
