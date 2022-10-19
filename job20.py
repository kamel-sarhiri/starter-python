
#définition de la fonction
def myAddition(a,b):
    return a+b

#déclaration nombre 1
num1 = input("Entrez le premier nombre entier pour l'addition : ")
num1=int(num1)

#déclaration nombre 2
num2 = input("Entrez le deuxième nombre entier pour l'addition :")
num2=int(num2)

#appel de la fonction et affichage du résultat
result = myAddition(num1,num2)
print("la somme =",result)