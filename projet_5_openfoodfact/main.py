from P5.Dbmanagement import Db_management
from P5.Api import Api

if __name__ == '__main__':
    ap = Api()
    ap.clean_product()
    data = Db_management()
    data.insert_categories()
    data.insert_product()


