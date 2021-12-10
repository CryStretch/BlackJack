from Paquet import piocheCarte, valeurCarte
import continues

def tourJoueur(j,paquet, dicoScores, listeJoueur):
    score=dicoScores[j]

    print("** tour .",1," "*6,"Joueur :",j," "*6,"main actuelle :", score,"**")
    print("")

    condition=continues()

    if condition==True:
        carte=piocheCarte(paquet,1)
        nb=valeurCarte(carte[0])
        score=nb+score

        if score==21:
            print("")
            return score

        elif score>21:
            listeJoueur.remove(j)
            print("perdant",listeJoueur)
            print ("Vous avez dépassé 21 vous avez perdu")
            print("")
            return score


        else:
            print ("Votre nouvelle main est :",score)
            print("")
            return score

    else:
        print("coucher",listeJoueur)
        listeJoueur.remove(j)
        print ("Vous avez décidé de vous coucher")
        print("")
        return score
