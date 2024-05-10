from db_connection import connect_db, Error
from customer_fetch import fetch_all_customers

def delete_customer(id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "DELETE FROM Customer WHERE id = %s"

            cursor.execute(query, (id,))
            conn.commit()
            print('Successfully Deleted Customer!')

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()



def delete_customer_wno(id):
    conn = connect_db()
    if conn is not None:
        try: 
            cursor = conn.cursor()

            query = "SELECT * FROM Orders WHERE customer_id = %s;" #Query our databse for orders associated with the user we are trying to delete
            cursor.execute(query, (id,))
            orders = cursor.fetchall() #if this returns an empty list [] we no this user had no orders, else they did and should be deleted
            if not orders:
                query = "DELETE FROM Customer WHERE id = %s"

                cursor.execute(query, (id,))
                conn.commit()
                print('Successfully Deleted Customer!')
            else:
                print("Cannot delete a user who has associated orders!")


            for row in cursor.fetchall():
                print(f"{row[0]}.) {row[1]}'s Contact info Email: {row[2]} Phone: {row[3]}.")

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

