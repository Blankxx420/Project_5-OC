"""this file contains all interface in command lines"""
from openfoodfacts.dbmanagement import Dbmanagement


class Openfoodfact:
    """this class making interface in command lines"""

    def __init__(self):
        """initiation of class Dbmanagement"""
        self.data = Dbmanagement()

    def home(self):
        """Basically menu function """
        self.data.return_categories()
        choice_cat = int(input("Veuillez entrer le numéro de la catégorie "
                               "souhaitée.\n"
                               ">>>"))
        print(choice_cat)
        self.data.return_product(choice_cat)
        choice_prod = int(input("Veuillez sélectionner un "
                                "produit en entrant son ID.\n"
                                ">>>"))
        self.data.select_product(choice_prod)
        self.keep_substitute(choice_prod, choice_cat)
        self.show_fav()

    def choice_sub(self, choice_prod, choice_cat):
        """ return substitute if choice is correct if not call home() """
        choice_sub = int(input("Souhaitez vous un substitut "
                               "avec ce produits ?\n"
                               "1. oui\n2. non\n"
                               ">>>"))
        if choice_sub == 2:
            self.home()
        if choice_sub == 1:
            print("Voici le substitut:\n")
            substitutes = self.data.return_substitute(choice_prod, choice_cat)
            for sub in substitutes:
                sub_id = sub[0]
                id_p, name, description, url, nutriscore, store = sub
                print(f"Id: {id_p}\n"
                      f"Nom: {name}\n"
                      f"Description: {description}\n"
                      f"Lien: {url}\n"
                      f"Nutri-score: {nutriscore}\n"
                      f"Magasin: {store}\n")
                return sub_id

    def keep_substitute(self, choice_prod, choice_cat):
        """Answer the use if he want keep product if it's yes
        it's save id of both product in database"""
        substitute = self.choice_sub(choice_prod, choice_cat)
        keep_sub = int(input("Souhaitez vous le sauvegarder dans "
                             "la base de donnée ?\n 1.oui\n2. non"))
        sub = substitute
        if keep_sub == 1:
            self.data.insert_substitute(sub, choice_prod)
            print("le produit est bien sauvegarder !")
        if keep_sub == 2:
            self.home()

    def show_fav(self):
        menu_fav = int(input('Souhaitez vous accéder à vos favoris\n'
                             '1. oui\n2. non\n'
                             '>>>'))
        if menu_fav == 1:
            self.data.show_favorite()
            self.del_favorite()
        if menu_fav == 2:
            self.home()

    def home_menu(self):
        """menu of launch of application"""
        print('******BIENVENUE******')
        print('********SUR**********')
        print('****OPEN FOOD FACT****')
        menu_choice = int(input("1. Souhaitez-vous remplacer un produit ? \n"
                                "2. Accéder à mes favoris.\n"
                                ">>> "))
        if menu_choice == 1:
            self.home()
        if menu_choice == 2:
            self.show_fav()

    def delete_favorites(self):
        """menu of deleting of all favorites"""
        del_favorites = int(input("voullez vous supprimer tout les favoris\n"
                                  "1. oui\n2. non\n"
                                  ">>>"))
        if del_favorites == 1:
            self.data.delete_all_fav()
        if del_favorites == 2:
            self.home_menu()

    def del_favorite(self):
        """menu of deleting one select favorite"""
        menu_del_favorite = int(input("voullez vous supprimer un favoris\n"
                                      "1. oui\n2. non\n"
                                      ">>>"))
        if menu_del_favorite == 1:
            fav_prod = int(input("Veuillez indiquer l'id du produit\n"
                                 ">>>"))

            fav_sub = int(input("Veuillez entre l'id du substitut au"
                                " produit\n"
                                ">>>"))

            self.data.delete_favorite(fav_prod, fav_sub)

        if menu_del_favorite == 2:
            self.delete_favorites()
