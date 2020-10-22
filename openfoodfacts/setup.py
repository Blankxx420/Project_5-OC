from openfoodfacts.dbmanagement import Dbmanagement


def setup():
    data = Dbmanagement()
    data.init_database()
    data.insert_categories()
    data.insert_product()


setup()
