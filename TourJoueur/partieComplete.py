import premierTour,partieFinie,tourComplet
from Joueurs_Scores import gagnant


def partieComplete(listeJoueur,p,dicoVictoire):
    dicoScores=premierTour(listeJoueur,p)
    

    while partieFinie(listeJoueur,dicoScores)==False:
        tourComplet(listeJoueur,dicoScores,p)
        
    winner,s=gagnant(dicoScores)
    print(winner,"vous êtes le gagnant !")
    
    dicoVictoire[winner]+=1
    
    return dicoVictoire

#si mec pioche 2 as à 11 il joue avec 22