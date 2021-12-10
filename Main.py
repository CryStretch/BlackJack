from Joueurs_Scores import initJoueurs
from Paquet import initPioche
from TourJoueur import partieComplete


#Main

n=int(input("combien de joueurs ?"))
listeJoueur=initJoueurs(n)

dicoVictoire={}
for e in listeJoueur:
    dicoVictoire[e]=0


rejouer="oui"

while rejouer=="oui":
     
    p=initPioche(len(listeJoueur))

    tabVictoire=partieComplete(listeJoueur,p,dicoVictoire)
    print("Tableau des scores :")
    print(tabVictoire)

    rejouer=input("voulez-vous rejouer 1 partie ? (oui/non)")

    listeJoueur=[]
    for j in tabVictoire.keys():
        listeJoueur.append(j)

#problème quand il y a blackjack dans certaines condition la partie ne s'arrete pas immédiatement
#quand quelqu'un perd (au dessus de 21) le poto après ce fais skip