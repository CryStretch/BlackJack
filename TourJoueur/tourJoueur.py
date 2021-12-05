from continues import *
def tourJoueur(j,p):
    i=1
    total=0 #à remplacer plus tard, pour l'instant c'est pour test la fonction

    print("** tour :",i," "*6,"Joueur :",j," "*6,"main actuelle :",total,"**")

    condition=continues()


    if condition==True:
        nb=piocheCarte(valeurCarte(p,1)) #1 valeur par déf on peut mettre variable que l'on demande à l'utilisateur
        total=nb+total
        return total

    #if total>21 or condition==False:
        #listeJoueur.remove(j)
        #return listeJoueur
        

            
