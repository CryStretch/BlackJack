def valeurCarte(carte):
    if 48<ord(carte[0])<58:
        nbCarte=int(carte[0]+carte[1])

    elif carte[0]=="v" or carte[0]=="d" or carte[0]=="r":
        nbCarte=10

    elif carte[0]=="a":
        nbCarte=int(input("Valeur souhaitee pour l'as ? (1 ou 11)"))

        while nbCarte!=1 and nbCarte!=11:
            nbCarte=int(input("Valeur incorrecte, valeur souhaitee pour l'as ? (1 ou 11)"))

    return nbCarte



#def valeurCarte(carte):
    for e in carte:
        carteVa=e[0]
        if carteVa[0]=="v" or carteVa[0]=="d" or carteVa[0]=="r":
            nbCarte=10

        if carteVa[0]=="a":

            nbCarte=int(input("quelle valeur pour l'as ? (1 ou 11)"))



            while nbCarte!=1 and nbCarte!=11:
                nbCarte=int(input("valeur incorrect, quelle valeur pour l'as ? (1 ou 11)"))



        if 48<ord(carteVa[0])<58:
            nbCarte=int(e[0]+e[1])

    return nbCarte

