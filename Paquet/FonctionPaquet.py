def paquet():
    figure=["2","3","4","5","6","7","8","9","10","valet", "dame", "roi", "as"]
    paquet=[]
    figure2=[" de carreau"," de coeur"," de trefle"," de pique"]
    for e in (figure2):
        for i in (figure):
            fig=i+e
            paquet.append(fig)
    return paquet
