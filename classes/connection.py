import pymysql.cursors
print("imported module")

connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            database='biblioteca',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
def get_connection():
    """
    This subprocess returns the connection to the database.
    """
    return connection
    # return connection