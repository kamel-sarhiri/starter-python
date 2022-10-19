def myupper(a): #définition de la fonction myupper
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïABCDEFGHIJKLMNOPQRSTUVWXYZAAEEEEII' #création de la variable alpahabet avec les caractéres minuscules et majuscules et remplacement des lettres minuscules ayant un accent
    result = '' #création de la variable résult 
    for x in a: 
        if x not in alphabet or alphabet.index(x)>=34:
            result += x
        else:
            result += alphabet[alphabet.index(x)+34]
    return result

def mylower(b):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in b:
        if x not in alphabet or alphabet.index(x)<=26:
            result += x
        else:
            result += alphabet[alphabet.index(x)-26]
    return result


def mytitle(c):
    words=c.split()
    result= ''

    for x in range(len(words)):
        carac=words[x][0]

        titre=myupper(carac)+words[x][1:]
        result += titre +" "
    return result

def myclean(d):
    words=d.split()
    result= ''

    for x in range(len(words)):
        result += words [x] + " "
    return result


texte= input ("Veuillez entrer un texte :")
param= input("veuillez entrer un des paramètres suivants: upper / lower / title / clean :")

while param!="upper" and param!="lower" and param!="title" and param!="clean": #si la valeur entrée est incorrecte, le programme demande à l'utilisateur d'entrer un paramètre juste
    print ("valeur incorrecte")
    param= input("veuillez choisir un des paramètres suivant: upper / lower / title / clean :")


if param == "upper":
    print(myupper(texte))
elif param == "lower":
    print(mylower(texte))
elif param == "title":
    print(mytitle(texte))
elif param == "clean":
    print(myclean(texte))