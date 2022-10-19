
def tris(*args) :
    myList = [] # creer une liste myList
    for i in args :
        myList.append(i) # ajoute les i les un à la suite dans myList
    myList.sort() # tri les paramètres dans l'odre croissant
    print (myList)
tris(56, 33, 21, 47, 99, 61)