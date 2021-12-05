def valeurCarte(carte):
    for e in carte:
        carteVa=e[0]
        if carteVa[0]=="v":
            nbCarte=11
        elif carteVa[0]=="d":
            nbCarte=12
        elif carteVa[0]=="r":
            nbCarte=13

        if carteVa[0]=="a":
            nbCarte=int(input("quelle valeur pour l'as ? (1 ou 11)"))
            while nbCarte!=1 or nbCarte!=11:
                nbCarte=int(input("valeur incorrect, quelle valeur pour l'as ? (1 ou 11)"))


        if 48<ord(carteVa[0])<58:
            nbCarte=int(e[0]+e[1])

    return nbCarte