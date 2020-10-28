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
                               "souhaitée."))
        print(choice_cat)
        self.data.return_product(choice_cat)
        choice_prod = int(input("Veuillez sélectionner un "
                                "produit en entrant son ID."))
        self.data.select_product(choice_prod)
        self.keep_substitute(choice_prod, choice_cat)
        self.show_fav()

    def choice_sub(self, choice_prod, choice_cat):
        """ return substitute if choice is correct if not call home() """
        choice_sub = input("Souhaitez vous un substitut avec ce produits ?"
                           " (oui, non)")
        if choice_sub == 'non':
            self.home()
        if choice_sub == 'oui':
            print("Voici le substitut:")
            substitutes = self.data.return_substitute(choice_prod, choice_cat)
            for sub in substitutes:
                sub_id = sub[0]
                result = str(sub).strip('()').replace("'", "")
                print(result)
                print(sub_id)
                return sub_id

    def keep_substitute(self, choice_prod, choice_cat):
        """Answer the use if he want keep product if it's yes
        it's save id of both product in database"""
        substitute = self.choice_sub(choice_prod, choice_cat)
        keep_sub = str(input("Souhaitez vous le sauvegarder dans "
                             "la base de donnée ? (oui/non)"))
        sub = substitute
        if keep_sub == 'oui':
            self.data.insert_substitute(sub, choice_prod)
            print("le produit est bien sauvegarder !")
        if keep_sub == 'non':
            self.home()

    def show_fav(self):
        menu_fav = input('Souhaitez vous accéder à vos favoris (oui, non)')
        if menu_fav == 'oui':
            self.data.show_favorite()
        if menu_fav == 'non':
            self.home()

    def home_menu(self):
        print('******BIENVENUE******')
        print('********SUR**********')
        print('****OPEN FOOD FACT****')
        menu_choice = input('Sélectionner le menu souhaité (menu, favoris)')
        if menu_choice == 'menu':
            self.home()
        if menu_choice == 'favoris':
            self.show_fav()
