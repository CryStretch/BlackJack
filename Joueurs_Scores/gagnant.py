def gagnant(scores):
    t=0
    for e in scores:
        if scores[e]>t:
            winner=scores[e]
        t=scores[e]

    return winner