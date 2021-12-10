from Joueurs_Scores import initScores
from Paquet import piocheCarte,valeurCarte

def premierTour(joueurs,p):
    dicoScores=initScores(joueurs)

    for e in joueurs:
        listeCarte=piocheCarte(p,2)

        Vcarte1=valeurCarte(listeCarte[0],e)
        Vcarte2=valeurCarte(listeCarte[1],e)
        S=Vcarte1+Vcarte2

        if S==22:
            S=12
    
        dicoScores[e]=S

    return dicoScores
