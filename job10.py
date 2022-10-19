
texte= input ("Veuillez entrer un texte :")
file = open("output.txt", "w") # Pour ouvrir un fichier, on utilise la fonction "open" et le mode 'w', qui signifie "write" pour écrire
file.write(texte) #récupère le texte écrit par l'utilisateur pour l'insérer dans le fichier output.txt
file.close() #Fermeture du fichier