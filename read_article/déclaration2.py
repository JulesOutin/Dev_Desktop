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

while True:
    # Demande de l'entrée de l'utilisateur
    user_input = input("Veuillez saisir un nombre entre 1 et 17: ")

    # Vérification de l'entrée de l'utilisateur
    if user_input.isdigit():
        article_number = int(user_input)
        if 1 <= article_number <= 17:
            # Affichage de l'article correspondant
            print(f"Article {article_number} : {articles[article_number]}")
            break
        else:
            print("Votre entrée est incorrecte. Veuillez saisir un nombre entre 1 et 17.")
    else:
        print("Votre entrée est incorrecte. Veuillez saisir un nombre entre 1 et 17.")
