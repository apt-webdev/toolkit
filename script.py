import os
import sqlite3

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join('db', 'evaluation.bin')

def getDataDB(cursor):

    return;

def openConnection():
    conn = sqlite3.connet(my_file)
    cursor = conn.cursor()
    return cursor, conn

def closeConnection(c, con):
    c.close()
    con.close()

class Script():
    cursor, conn = openConnection()

    getDataDB(cursor)

    closeConnection(cursor, conn)


if __name__ == "__main__":
    Script()