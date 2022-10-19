#créatrion de l'input
nb=int(input("Entrez un nombre entier :"))
f = open("data.txt", "r")  #ouverture du fichier data.txt en mode lecture seule et création de f
file = f.read() #création du param file

list = file.split()
wordcount = 0 #initialisation de la variable wordcount
for i in range (len(list)) :
    if len(list[i]) == nb :
        wordcount += 1
f.close() # fermeture de f

print ("il y a", wordcount, "mots de", nb,"lettres dans le fichier")

