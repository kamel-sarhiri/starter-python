# Récupération de la largeur et de la hauteur saisies par l'utilisateur
largeur = int(input("Saisissez la largeur du rectangle : "))
hauteur = int(input("Saisissez la hauteur du rectangle : "))

# Boucle pour dessiner le rectangle
for i in range(hauteur):
    if i == 0 or i == hauteur-1:  # si on est sur la première ou la dernière ligne
        print("-" * largeur)  # on dessine la ligne horizontale
    else:
        print("|" + " " * (largeur-2) + "|")  # on dessine les côtés verticaux avec des espaces

