largeur = int(input("entrez la largeur du rectangle :"))
hauteur = int(input("entrez la hauteur du rectangle :"))

for i in range (hauteur) :
    if i == 0 or i == hauteur-1 :
        print ("|", end="") # le "end="" permet de mettre les caractères à la suite sans sauter la ligne
        for i in range (largeur-2) :
            print ("-", end="")
        print ("|")

    else :
        print ("|", end="")
        for i in range (largeur-2) :
            print (" ", end="")
        print ("|")
