"""this file contains all interface in command lines"""
from openfoodfacts.dbmanagement import Dbmanagement


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
        self.keep_substitute(choice_prod, choice_cat)

    def choice_sub(self, choice_prod, choice_cat):
        """ return substitute if choice is correct if not call home() """
        choice_sub = str(input("Souhaitez vous un substitut avec ce produits ? (oui, non)"))
        if choice_sub == 'non':
            self.home()
        if choice_sub == 'oui':
            print("Voici le substitut:")
            substitute = self.data.return_substitute(choice_prod, choice_cat)
            for sub in substitute:
                result = str(sub).strip('()').replace("'", "")
                print(result)
                return sub

    def keep_substitute(self, choice_prod, choice_cat):
        """Answer the use if he want keep product if it's yes it's save id of both product in database"""
        substitut = self.choice_sub(choice_prod, choice_cat)
        keep_sub = str(input("Souhaitez vous le sauvegarder dans la base de donnée ? (oui/non)"))
        sub = substitut[0]
        if keep_sub == 'oui':
            self.data.insert_substitute(sub, choice_prod)
            print("le produit est bien sauvegarder !")
        if keep_sub == 'non':
            self.home()
