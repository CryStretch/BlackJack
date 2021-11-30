def initJoueurs(n):
    listeJoueur=[]
    while n>0:
        nomJoueur=input("Nom du joueur :")
        listeJoueur.append(nomJoueur)
        n-=1
    return listeJoueur
