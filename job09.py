hauteur = int(input("Entrez la hauteur du triangle : "))

for i in range(hauteur):
    if i == hauteur -1 :
        print('/'+'_' * ((hauteur*2)-2)+'\\')
    else:
        print(' ' * (hauteur - i -1 ) + '/' + ' ' * (2*i) + '\\')