def valeurCarte(carte):

    if carte[0]=="v":
        nbCarte=11
    elif carte[0]=="d":
        nbCarte=12
    elif carte[0]=="r":
        nbCarte=13


    if carte[0]=="a":
        nbCarte=int(input("quelle valeur pour l'as ? (1 ou 11)"))
        while nbCarte!=1 or nbCarte!=11:
            nbCarte=int(input("valeur incorrect, quelle valeur pour l'as ? (1 ou 11)"))

    if 48<ord(carte[0])<58:
        nbCarte=int(carte[0]+carte[1])

    return nbCarte
