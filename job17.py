
def nbpaire(*args) :
    myList = [] # creer une liste myList
    for i in args :
        myList.append(i)

    
    for i in myList : 
        if i % 2 == 0 : # condition sur les nombres paires
            print(i)

nbpaire(1, 2, 3, 4, 5, 6, 7, 8, 9)        