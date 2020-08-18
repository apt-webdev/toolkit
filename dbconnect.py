import sqlite3


# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join('db', 'evaluation.bin')
class DBConnect:

    @staticmethod
    def open_connection(filename):
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def get_data_db(cursor):
        return

    @staticmethod
    def load_data(cursor):
        cursor.execute("select * from Activity_Log")
        rows = cursor.fetchall()

    @staticmethod
    def close_connection(conn, cursor):
        conn.close()
        cursor.close()
