def gagnant(scores):
    dico=dict(scores) #on fait une copie profonde du dico
    for i in scores:
        if scores[i]>21:
            dico.pop(i) #on supprime dans la copie pour ne pas faire d'effet de bord
    x=list(dico.values()) #on fait une liste des valeurs du dico
    y=list(dico.keys())
    e=1
    c=0
    maxx=x[0]
    maxi=21
    while e<len(x):
        if maxx==maxi:
            return (y[0],maxi)
        elif x[e]==maxi:
            return (y[e],maxi)
        elif x[e]>maxx:
            maxx=x[e]
            c=e
        e+=1
    return (y[c],maxx)