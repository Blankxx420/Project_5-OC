# [Project_5-OC](https://openclassrooms.com/fr/paths/68/projects/157/assignment)
## Utiliser les données publiques de l'OpenFoodFact!![Image of Openfoodfact](Images/Open_Food_Facts_logo.svg.png)
La startup Pur Beurre travaille connait bien les habitudes alimentaires françaises. Leur restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs sur la butte de Montmartre.

L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer. Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ? Leur idée est donc de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

## :book: Cahiers des charges
**L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :**

1. **Quel aliment souhaitez-vous remplacer ?**
2. **Retrouver mes aliments substitués.**

- **Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :**
- **Sélectionnez la catégorie.** *[Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]*
- **Sélectionnez l'aliment**. *[Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]*
- **Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.**
- **L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.**
## :wrench: Installation 
1. **Installer [MYSQL](https://dev.mysql.com/downloads/installer/)**
2. **Créer votre base de données MYSQL**
3. **Remplacer les identifiant de la base de données pour la connexion dans constant.py**
```
DB_NAME, DB_USER, DB_PASS
```
4. **Lançer setup.py**
```
python -m openfoodfacts.setup
```
5. **Lançer main.py**
```
python -m openfoodfacts.main
```
6. **ENJOY!** :smiley:

## :round_pushpin: Diagramme 
![Image of Openfoodfact](Images/database_diagram.png)
---
## :round_pushpin: [Trello](https://trello.com/b/uBhCgrdO/projet-5)
![Image of Openfoodfact](Images/trello.png)

