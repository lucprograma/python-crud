import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes'))
)
import connection
def update(squema) -> None:
    try:
        connect = connection.get_connection()
        with connect.cursor() as cursor:
            query = "UPDATE categories SET name=%s WHERE id_category = %s"
            cursor.execute(query, (squema['name'], squema['id']))
            print("registro modificado")
            connect.commit()
    except Exception as e:
        print("Ocurrio un error", e)
    finally:
        connect.close()