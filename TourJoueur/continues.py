def continues():
    rep=input("Veux-tu continuer de jouer ? (oui/non)")
    while rep!="oui" and rep!="non":
        rep=input("Je n'ai pas compris la réponse, veux-tu continuer de jouer ? (oui/non)")
    if rep=="oui":
        return True
    else:
        return False