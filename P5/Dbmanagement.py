import mysql.connector
from P5.Api import Api
from P5.Setup import CATEGORIES_LIST
import random


class Dbmanagement:

    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='root',
            password='Enurox123',
            host='localhost',
            database='mydb',
        )
        self.result = []

    def insert_categories(self):
        cursor = self.cnx.cursor()
        sql_insert_cat = "INSERT IGNORE INTO Category (name) VALUES (%(category)s)"
        for category in CATEGORIES_LIST:
            category_to_add = {'category': category}
            cursor.execute(sql_insert_cat, category_to_add)
        self.cnx.commit()
        cursor.close()

    def return_categories(self):
        cursor = self.cnx.cursor()
        sql_return_cat = "SELECT * FROM Category"
        cursor.execute(sql_return_cat)
        fetch = cursor.fetchall()
        for rows in fetch:
            for word in rows:
                result = str(word).strip("(')")
                print(result)
        cursor.close()

    def insert_product(self):
        cursor = self.cnx.cursor()
        sql_insert_prod = (
            "INSERT IGNORE INTO Product (barcode, name, description, store, link, nutriscore, category_id)"
            "VALUES(%(code)s, %(product_name)s, %(details)s, %(stores)s, %(link)s, %(nutriscore)s,"
            " (SELECT id from Category WHERE name = %(categories)s))"
        )
        prod = Api()
        prod.clean_product()
        for item in prod.product_list:
            cursor.execute(sql_insert_prod, item)
        self.cnx.commit()
        cursor.close()

    def return_product(self, choice_cat):
        cursor = self.cnx.cursor()
        sql_return_prod = "SELECT id,name,description,link,nutriscore,store FROM Product WHERE category_id = %(choice)s ORDER BY RAND() LIMIT 10"

        cursor.execute(sql_return_prod, {'choice': choice_cat})
        fetch = cursor.fetchall()
        print(fetch)


    def insert_substitute(self, product):
        cursor = self.cnx.cursor()
        sql_insert_sub = (
            "INSERT IGNORE INTO subtitute (product_id) VALUES (SELECT id from Product WHERE id = %(product)s))"
        )
        cursor.execute(sql_insert_sub, product)


if __name__ == '__main__':
    data = Dbmanagement()
    data.insert_categories()
    data.insert_product()
