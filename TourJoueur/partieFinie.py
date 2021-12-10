def partieFinie(listeJoueur,dicoScores):
    for e in listeJoueur:
        print(e)
        if dicoScores[e]==21 or len(listeJoueur)==1:
            return True
        else:
            cond=False
    return cond