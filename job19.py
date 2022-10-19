

def tri(*args):
    mylist = [] # creer une liste myList
    for i in args:
         mylist.append(i)

    for i in range(len(mylist)):
         for j in range(i + 1, len(mylist)): #trier sans utiliser la fonction sort

            if mylist[i] > mylist[j]:
                mylist[i], mylist[j] = mylist[j], mylist[i]
    print(mylist)
tri(56, 33, 21, 47, 99, 61)