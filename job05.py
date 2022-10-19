#  Les boucles For

#déclaration des variables
Input1=int(input("entrez un nombre  :"))
Input2=int(input("entrez un nombre  :"))

if Input1 < Input2 :
    for i in range(Input1+1 , Input2) : #Boucle for pour incrémenter de un entre les deux bornes
        print (i)

elif Input1 > Input2 :
    for i in range(Input1-1 , Input2 , -1) : #Boucle for pour désincrémenter de un en partant de la valeur 1 vers la valeur 2
        print (i)

else :
    print ("valeurs égales")