"""this file contains all interface in command lines"""
from projet_5_openfoodfact.dbmanagement import Dbmanagement


class Openfoodfact:
    """this class making interface in command lines"""

    def __init__(self):
        """initiation of class Dbmanagement"""
        self.data = Dbmanagement()

    def home(self):
        """Basically menu function """
        print('******BIENVENUE******')
        print('********SUR**********')
        print('****OPEN FOOD FACT****')
        self.data.return_categories()
        choice_cat = int(input("Veuillez entrer le numéro de la catégorie souhaitée."))
        print(choice_cat)
        self.data.return_product(choice_cat)
        choice_prod = int(input("Veuillez sélectionner un produit en entrant son ID."))
        self.data.select_product(choice_prod)
        self.choice_sub(choice_prod, choice_cat)

    def choice_sub(self, choice_prod, choice_cat):
        """ return substitute if choice is correct if not call home() """
        choice_sub = str(input("Souhaitez vous un substitut avec ce produits ? (oui, non)"))
        if choice_sub == 'non':
            self.home()
        if choice_sub == 'oui':
            print("Voici le substitut:")
            self.data.return_substitute(choice_prod, choice_cat)


op = Openfoodfact()
op.home()


