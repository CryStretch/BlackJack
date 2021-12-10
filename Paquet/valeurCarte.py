def valeurCarte(carte,j):
    if 48<ord(carte[0])<58:
        nbCarte=int(carte[0]+carte[1])

    elif carte[0]=="v" or carte[0]=="d" or carte[0]=="r":
        nbCarte=10

    elif carte[0]=="a":
        print("joueur :",j)
        nbCarte=int(input("Valeur souhaitee pour l'as ? (1 ou 11)"))

        while nbCarte!=1 and nbCarte!=11:
            nbCarte=int(input("Valeur incorrecte, valeur souhaitee pour l'as ? (1 ou 11)"))

    return nbCarte



