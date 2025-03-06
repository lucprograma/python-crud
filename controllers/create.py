
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes'))
)
import connection
def create_register(name):
    print("Something")
    new_connection = connection.get_connection()
    try:
        with new_connection.cursor() as cursor:
            query = "insert into categories(name) values (%s)"
            cursor.execute(query, name)
            print("Created register!")
    except:
        print("No se pudo crear el registro")
    new_connection.commit()