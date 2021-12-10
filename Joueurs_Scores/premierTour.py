from Joueurs_Scores import initScores
from Paquet import piocheCarte, valeurCarte


def premierTour(joueurs,p):
    dicoScores=initScores(joueurs)


    for e in joueurs:
        listeCarte=piocheCarte(p,2)

        Vcarte1=valeurCarte(listeCarte[0])
        Vcarte2=valeurCarte(listeCarte[1])
        S=Vcarte1+Vcarte2
        dicoScores[e]=S

    return dicoScores