with open("c:/Users/sarhi/Desktop/la plateforme/python/data.txt") as f: #ouverture du fichier domains.xml en mode lecture seule

    contents = f.read() # lecture du contenu du fichier à l’aide de la fonction read() et stockage dans une variable contents
    words = contents.split() # utilisation de la fonction split 
    wordscount = len(words)
    print ("le nombre de mot est :", wordscount) # affichage du compte
f.close() #fermeture du fichier f