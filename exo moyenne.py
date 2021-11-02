acc=0
i=0
note=float(input("entrer une note : "))
meilleurNote=0
pireNote=20


while 0<=note<=20:

    if meilleurNote<note:
        meilleurNote=note
    elif pireNote>note:
        pireNote=note

    noteF=note+i
    i=noteF
    acc=acc+1
    note=float(input("entrer une nouvelle note : "))


if acc==0:
    print("tu n'as pas rentré une note correct")
else:
    moyenne=noteF/acc
    print(moyenne)
    print("t'as meilleur note :",meilleurNote)
    print("t'as pire note:",pireNote)

input("")