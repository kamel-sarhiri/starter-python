def mysort(mylist): #définition de la fonction mysort 
    for i in range(len(mylist)): #pour i allant de 0 à la longueur de mylist
         for j in range(i + 1, len(mylist)): #trier sans utiliser la fonction sort
            if mylist[i] > mylist[j]:
                mylist[i], mylist[j] = mylist[j], mylist[i]
    print(mylist)

def mydisplay(display): #définition de la fonction mydisplay
    print(display)

s=[6,12,56,32,41] #déclaration de la liste s
d=[23,54,2,14,20] #déclaration de la liste d

mysort(s) #appel de la fonction mysort
mydisplay(d) #appel de la fonction display