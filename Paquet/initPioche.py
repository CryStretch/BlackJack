import Paquet
from random import shuffle

def initPioche(n):
    melange1=[]
    for i in range(n):
        melange1.append(Paquet())
        melange=[]
        e=0

    while e<len(melange1):
        melange+=melange1[e]
        e+=1
    shuffle(melange)  
 
    return (melange)