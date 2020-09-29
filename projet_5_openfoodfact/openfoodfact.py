from projet_5_openfoodfact.dbmanagement import Dbmanagement


class Openfoodfact:

    def __init__(self):
        self.data = Dbmanagement()

    def home(self):
        print('******BIENVENUE******')
        print('********SUR**********')
        print('****OPEN FOOD FACT****')
        self.data.return_categories()
        choice_cat = int(input("Veuillez entrer le numéro de la catégorie souhaitée."))
        print(choice_cat)
        self.data.return_product(choice_cat)
        self.product_choice()
        self.choice_sub()

    def product_choice(self):
        choice_prod = int(input("Veuillez sélectionner un produit en entrant son ID."))
        for item in self.data.result:
            for i in item:
                if i == choice_prod:
                    print('Voici le produit sélectionné.')
                    print(str(item).strip('()').replace("'", ""))

    def choice_sub(self):
        choice_sub = str(input("Souhaitez vous un substitut avec ce produits ? (oui, non)"))
        if choice_sub == 'non':
            self.home()
        if choice_sub == 'oui':
            print("Voici le substitut:")


op = Openfoodfact()
op.home()


