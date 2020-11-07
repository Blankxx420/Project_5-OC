"""
this file is all interaction with database using my sql.connector
"""
import mysql.connector

from openfoodfacts.api import Api
from openfoodfacts.constant import CATEGORIES_LIST, DB_USER, DB_PASS, DB_NAME


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

    def init_database(self):
        """read the sql script and create the database"""
        with open("openfoodfacts/Database_script.sql") as sqlfile:
            content = sqlfile.read()
        sql_requests = [sql for sql in content.split(';') if sql.strip()]
        cursor = self.cnx.cursor()
        for sql_request in sql_requests:
            cursor.execute(sql_request)

    def insert_categories(self):
        """inserting categories in database by browse CATEGORIES_LIST"""
        cursor = self.cnx.cursor()
        sql_insert_cat = ("INSERT IGNORE INTO Category (name) "
                          "VALUES (%(category)s)"
                          )
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
            id_c, category = rows
            print(f"{id_c}: {category}")

        cursor.close()

    def insert_product(self):
        """inserting product in database, using product_list in Api"""
        cursor = self.cnx.cursor()
        sql_insert_prod = (
            "INSERT IGNORE INTO Product "
            "(barcode,name,description,store,link,nutriscore, "
            "category_id) "
            "VALUES (%(code)s,%(product_name)s,%(details)s,%(stores)s, "
            "%(link)s, %(nutriscore)s,"
            "(SELECT id FROM Category WHERE name = %(categories)s))"
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
        sql_return_prod = ("SELECT id,name,description,link,nutriscore,store "
                           "FROM Product "
                           "WHERE category_id = %(choice)s "
                           "AND nutriscore >= 'c' "
                           "ORDER BY RAND() LIMIT 10")
        cursor.execute(sql_return_prod, {'choice': choice_cat})
        fetch = cursor.fetchall()
        for product in fetch:
            self.result.append(product)
            id_p, name, description, url, nutriscore, store = product
            print(f"Id: {id_p}\n"
                  f"Nom: {name}\n"
                  f"Description: {description}\n"
                  f"Lien: {url}\n"
                  f"Nutri-score: {nutriscore}\n"
                  f"Magasin: {store}\n")

    def select_product(self, choice_prod):
        """selecting product by id for selection of 1 product by user"""
        cursor = self.cnx.cursor()
        sql_select_product = ("SELECT id,name,description,link,nutriscore "
                              ",store "
                              "FROM Product WHERE id = %(choice_p)s"
                              )
        cursor.execute(sql_select_product, {'choice_p': choice_prod})
        fetch = cursor.fetchall()
        for product in fetch:
            id_p, name, description, link, nutri, store = product
            print(f"Voici le produit selectionné:\n\n"
                  f"Id: {id_p}\n"
                  f"Nom: {name}\n"
                  f"Description: {description}\n"
                  f"Lien: {link}\n"
                  f"Nutri-score: {nutri}\n"
                  f"Magasin: {store}\n")

    def insert_substitute(self, sub_id, choice_prod):
        """inserting id of product into table substitute"""
        cursor = self.cnx.cursor()
        sql_insert_sub = (
            "INSERT IGNORE INTO substitute (productsub_id, product_id) "
            "VALUES (%(substitute_id)s, %(product_id)s)"
        )
        cursor.execute(sql_insert_sub, {'substitute_id': sub_id,
                                        'product_id': choice_prod})
        self.cnx.commit()

    def return_substitute(self, choice_prod, choice_cat):
        """by selecting product return healthy product based
         on nutrition grades and category"""
        cursor = self.cnx.cursor()
        sql_return_grade = ("SELECT nutriscore FROM Product "
                            "WHERE id = %(product_id)s"
                            )
        cursor.execute(sql_return_grade, {'product_id': choice_prod})
        grade_aliment = cursor.fetchone()
        sql_return_sub = ("SELECT id,name,description,link,nutriscore,store "
                          "FROM Product "
                          "WHERE category_id = %(choice_c)s "
                          "AND nutriscore < %(grade)s "
                          "ORDER BY RAND() "
                          "LIMIT 1"
                          )
        cursor.execute(sql_return_sub, {'choice_c': choice_cat,
                                        'grade': grade_aliment[0]})
        result = cursor.fetchall()
        return result

    def show_favorite(self):
        """return product with associated substitute"""
        cursor = self.cnx.cursor()
        sql_show_fav = ("SElECT Product.id,Product.name,Product.description, "
                        "Product.link,Product.nutriscore,Product.store, "
                        "sub.id,sub.name,sub.description,sub.link, "
                        "sub.nutriscore,sub.store FROM substitute "
                        "JOIN Product on substitute.product_id = Product.id "
                        "JOIN Product as sub "
                        "on substitute.productsub_id = sub.id"
                        )
        cursor.execute(sql_show_fav)
        favorites = cursor.fetchall()
        for fav in favorites:
            products = fav[:6]
            substitute = fav[6:]
            p_id, p_name, p_description, p_url, p_nutri, p_store = products
            s_id, s_name, s_description, s_url, s_nutri, s_store = substitute
            print(f"le produit:\n"
                  f"Id: {p_id}\n"
                  f"Nom: {p_name}\n"
                  f"Description: {p_description}\n"
                  f"Lien: {p_url}\n"
                  f"Nutri-score: {p_nutri}\n"
                  f"Magasin: {p_store}\n"
                  f"\n"
                  f"peut être substitut par le produit:\n"
                  f"Id: {s_id}\n"
                  f"Nom: {s_name}\n"
                  f"Description: {s_description}\n"
                  f"Lien: {s_url}\n"
                  f"Nutri-score: {s_nutri}\n"
                  f"Magasin: {s_store}\n")

    def delete_all_fav(self):
        """deleting all favorites in table substitute"""
        cursor = self.cnx.cursor()
        sql_d_all_fav = (
            "DELETE FROM substitute"
        )
        cursor.execute(sql_d_all_fav)
        self.cnx.commit()
        print('tout les favoris on bien étés effacés')

    def delete_favorite(self, fav_prod, fav_sub):
        """delete one favorite  by getting by user id of product and substitute"""
        cursor = self.cnx.cursor()
        sql_del_fav = (
            "DELETE FROM substitute WHERE product_id = %(choice_fav_p)s "
            " AND productsub_id = %(choice_fav_s)s"
        )
        cursor.execute(sql_del_fav, {'choice_fav_p': fav_prod,
                                     'choice_fav_s': fav_sub
                                     }
                       )
        self.cnx.commit()
        print("le favoris à bien été effacé")
