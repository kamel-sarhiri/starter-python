with open("c:/Users/sarhi/Desktop/la plateforme/python/domains.xml") as f: #ouverture du fichier domains.xml en mode lecture seule
    contents = f.read() # lecture du contenu du fichier à l’aide de la fonction read() et stockage dans une variable contents
    count = contents.count("domain") # utilisation de la fonction count pour trouver l'occurence du mot "domain"
    print ("le nombre de domaine est :", count) # affichage du compte
    f.close() #fermeture du fichier f