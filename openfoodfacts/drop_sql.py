import mysql.connector


class Drop:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='Enurox123', host='localhost', database='mydb')

    def drop_all(self):
        cursor = self.cnx.cursor()
        cursor.execute("DROP TABLE subtitute")
        cursor.execute("DROP TABLE Product")
        cursor.execute("DROP TABLE Category")
        self.cnx.commit()
        cursor.close()


use = Drop()
use.drop_all()
