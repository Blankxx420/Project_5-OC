"""this files is use to make api calls and filtering data"""
import requests

from projet_5_openfoodfact.setup import CATEGORIES_LIST


class Api:
    def __init__(self):
        self.product_list = []

    def get_product(self):
        """Making api call by browsing category in CATEGORIES_LIST"""
        products = []
        for category in CATEGORIES_LIST:
            try:
                r = requests.get(
                    'https://fr.openfoodfacts.org/cgi/search.pl',
                    params={
                        'action': 'process',
                        'json': 1,
                        'countries': 'France',
                        'tag_0': category,
                        'sort_by': 'unique_scans_n',
                        'page_size': 100,
                        'page': 1,
                    },
                )
                r.raise_for_status()
            except requests.exceptions.RequestException:
                print("connexion error")
                products.append([])
                continue
            result = r.json()
            products.append(result['products'])
            return products

    def filter_data(self):
        """filtering data contained in product_by_category"""
        products_by_category = self.get_product()
        for products, category in zip(products_by_category, CATEGORIES_LIST):
            for product in products:
                try:
                    attributes = {
                        'product_name': product['product_name_fr'],
                        'nutriscore': product['nutrition_grades'],
                        'link': product['url'],
                        'code': product['code'],
                        'details': product['generic_name_fr'],
                        'stores': product['stores_tags'][0].strip(),
                        'categories': category,
                    }

                except (IndexError, KeyError):
                    continue

                self.product_list.append(attributes)

    def clean_product(self):
        """filtering empty keys in self.product_list"""
        self.filter_data()
        dict_keys = self.product_list[0].keys()
        for detail in self.product_list:
            for keys in dict_keys:
                if not detail[keys]:
                    try:
                        self.product_list.remove(detail)
                    except ValueError:
                        pass
