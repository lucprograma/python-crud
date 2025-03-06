import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes'))
)
import connection

def get_registers() -> dict:
    new_connection = connection.get_connection()
    try:
        with new_connection.cursor() as cursor:
            query = "SELECT * FROM categories"
            cursor.execute(query)
            return cursor.fetchall()
    except:
        print("Se ha producido un error")
        return dict()