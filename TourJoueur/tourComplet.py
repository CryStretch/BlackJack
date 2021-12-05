def tourComplet(listeJoueur):
    p=paquet()

    while len(listeJoueur)>0:

        for e in listeJoueur:
            total=tourJoueur(e)
            
            if total>21:
                listeJoueur.remove(e)
