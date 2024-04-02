# Importation de la bibliothèque os pour accéder aux fichiers
import os

# Création d'un dictionnaire vide pour stocker les articles
articles = {}

# Ouverture du fichier
with open(os.path.join("declaration1789.txt"), "r") as file:
    text = file.read().split("Art. ")

    # Parcours du texte et stockage des articles dans le dictionnaire
    for article in text[1:]:
        # Séparation du numéro de l'article et du texte
        number, text = article.split(".", 1)
        # Stockage de l'article dans le dictionnaire
        articles[int(number)] = text.strip()

# Affichage du dictionnaire
for number, article in articles.items():
    print(f"Article {number} : {article}")
