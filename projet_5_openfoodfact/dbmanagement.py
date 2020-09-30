"""
this file is all interaction with database using my sql.connector
"""
import mysql.connector

from projet_5_openfoodfact.api import Api
from projet_5_openfoodfact.setup import CATEGORIES_LIST, DB_USER, DB_PASS, DB_NAME


class Dbmanagement:
    """this class control of action made with MYSQL and database"""
    def __init__(self):
        """init for database connexion and creating list result"""
        self.cnx = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASS,
            host='localhost',
            database=DB_NAME,
        )
        self.result = []

    def insert_categories(self):
        """inserting categories in database by browse CATEGORIES_LIST"""
        cursor = self.cnx.cursor()
        sql_insert_cat = "INSERT IGNORE INTO Category (name) VALUES (%(category)s)"
        for category in CATEGORIES_LIST:
            category_to_add = {'category': category}
            cursor.execute(sql_insert_cat, category_to_add)
        self.cnx.commit()
        cursor.close()

    def return_categories(self):
        """Return all category id and name in database"""
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
        """inserting product in database, using product_list in Api"""
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
        """return 10 product randomly contain in category selected"""
        cursor = self.cnx.cursor()
        sql_return_prod = "SELECT id,name,description,link,nutriscore,store FROM Product WHERE category_id = %(choice)s ORDER BY RAND() LIMIT 10"
        cursor.execute(sql_return_prod, {'choice': choice_cat})
        fetch = cursor.fetchall()
        for i in fetch:
            self.result.append(i)
            rows = str(i).strip('()').replace("'", "")
            print(rows)

    def select_product(self, choice_prod):
        """selecting product by id for selection of 1 product by user"""
        cursor = self.cnx.cursor()
        sql_select_product = "SELECT id,name,description,link,nutriscore,store FROM Product WHERE id = %(choice_p)s"
        cursor.execute(sql_select_product, {'choice_p': choice_prod})
        fecth = cursor.fetchall()
        for i in fecth:
            for y in i:
                result = str(y).strip("(')")
                print(result)

    def insert_substitute(self, product):
        """inserting id of product into table substitute"""
        cursor = self.cnx.cursor()
        sql_insert_sub = (
            "INSERT IGNORE INTO subtitute (product_id) VALUES (SELECT id from Product WHERE id = %(product)s))"
        )
        cursor.execute(sql_insert_sub, product)

    def return_substitute(self):
        cursor = self.cnx.cursor()
        sql_return_sub = "Select id,name,description,link,nutriscore,store FROM Product"
        cursor.execute(sql_return_sub)


if __name__ == '__main__':
    data = Dbmanagement()
    data.insert_categories()
    data.insert_product()
