from TourJoueur import tourJoueur

def tourComplet(listeJoueur,dicoScore,p):
    for j in listeJoueur:
        print("La table Actuelle est :", dicoScore)
        print("")
        score=tourJoueur(j,p, dicoScore, listeJoueur)
        dicoScore[j]=score
        if score==21:
            break

