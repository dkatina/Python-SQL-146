from db_connection import connect_db, Error
from order_fetch import fetch_all_orders

def delete_order(id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "DELETE FROM Orders WHERE id = %s"

            cursor.execute(query, (id,))
            conn.commit()
            print('Successfully Deleted Order!')

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


