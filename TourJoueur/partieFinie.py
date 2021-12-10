def partieFinie(listeJoueur,dicoScores):
    for e in listeJoueur:
        print(e)
        if dicoScores[e]==21 or len(listeJoueur)==1:
            return True
        else:
            cond=False
    return cond

#manque condition pour arreter partie immédiatment quand joueur à 21