import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes'))
)
import connection

def delete(id: int) -> None:
    try:
        connect = connection.get_connection()
        with connect.cursor() as cursor:
            query = "DELETE from categories WHERE id_category=%s"
            cursor.execute(query, (str(id),))
            connect.commit()
            print("Registro borrado correctamente:", id)
    except:
        print("No se pudo borrar el registro", id)
    finally:
        connect.close()