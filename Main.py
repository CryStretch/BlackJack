#Partie A, initialisation

def paquet():
    figure=["2","3","4","5","6","7","8","9","10","valet", "dame", "roi", "as"]
    paquet=[]
    couleur=[" de carreau"," de coeur"," de trefle"," de pique"]
    for e in (couleur):
        for i in (figure):
            fig=i+e
            paquet.append(fig)
    return paquet




def valeurCarte(carte):
    for e in carte:
        carteVa=e[0] 
        if carteVa[0]=="v":
            nbCarte=10
        elif carteVa[0]=="d":
            nbCarte=10
        elif carteVa[0]=="r":
            nbCarte=10

        if carteVa[0]=="a":
            nbCarte=int(input("quelle valeur pour l'as ? (1 ou 11)"))
            while nbCarte!=1 or nbCarte!=11:
                nbCarte=int(input("valeur incorrect, quelle valeur pour l'as ? (1 ou 11)"))


        if 48<ord(carteVa[0])<58:
            nbCarte=int(e[0]+e[1])

    return nbCarte


#Fonction initPioche


def piocheCarte(p,x):
    main=[]
    for e in range(0,x):
        main.append(p[0])
        p.pop(0)

    return main





def initJoueurs(n):
    listeJoueur=[]
    while n>0:
        nomJoueur=input("Nom du joueur :")
        listeJoueur.append(nomJoueur)
        n-=1
    return listeJoueur





def initScores(joueurs,v):
    ScoresJoueurs={}
    for e in joueurs:
        ScoresJoueurs[e]=v
    return ScoresJoueurs


#Fonction premierTour


def gagnant(scores):
    t=0
    for e in scores:
        if scores[e]>t:
            winner=scores[e]
        t=scores[e]

    return winner


#Partie B, Gestion de la partie 



def continues():
    rep=input("veux-tu continuer de jouer ? (oui/non)")
    #while rep!="oui" or rep!="non":
        #rep=input("je n'ai pas compris la réponse, veux-tu continuer de jouer ? (oui/non)")
    if rep=="oui":
        return True
    else:
        return False






def tourJoueur(j,paquet):
    listeJoueur=["jean"] #liste pour test
    total=0 #à remplacer plus tard, pour l'instant c'est pour test la fonction (là tot toujours =nb pour tourComplet)
    i=1

    print("** tour :",i," "*6,"Joueur :",j," "*6,"main actuelle :",total,"**")

    condition=continues()


    if condition==True:
        nb=valeurCarte(piocheCarte(paquet,1)) #1 valeur par déf on peut mettre variable que l'on demande à l'utilisateur
        total=nb+total
        return total

    if total>21 or condition==False:
        #listeJoueur.remove(j)         dans tourComplet ou dans tourJoueur ?
        return False





def tourComplet(listeJoueur):
    p=paquet()

    while len(listeJoueur)>0:

        for e in listeJoueur:
            total=tourJoueur(e,p)

            if total>21 or total==False:
                listeJoueur.remove(e)
#création du paquet dans cette fonction mais 1 seul paquet pour la table à voir pour déplacer
#donc savoir où initialiser initPaquet(Paquet()) dans prog




liste=["Patrick","Jiji","Jean"]
print(tourComplet(liste))