#créatrion de l'input
H = int (input("remplir la hauteur "))

#dessiner le triangle
a=0
for i in range (H,1,-1): 
    print (" " * i, end="")
    print ("/", end="")
    print (" " * a * 2 + "\\")
    a = a+1


print (" /", end="")
#for i in range (H-1):
print ("__" *(H-1), end="")
print ("\\")