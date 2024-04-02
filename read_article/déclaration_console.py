with open('declaration1789.txt', 'r', encoding='utf-8') as file:
    # Lecture du contenu du fichier
    content = file.readlines()

# Demande à l'utilisateur de choisir un numéro entre 1 et 17
num = int(input("Choisissez un numéro entre 1 et 17 : "))

# Vérification de la validité du numéro choisi
if num < 1 or num > 17:
    print("Numéro invalide. Veuillez choisir un numéro entre 1 et 17.")
else:
    # Affichage du texte correspondant au numéro choisi
    print(content[num - 1])