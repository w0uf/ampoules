

class ampoule:
     def __init__(self,nb, etat=False):
         self.nb=nb
         self.etat=etat


def create_liste():
    from random import shuffle
         
    retour= [i+1 for i in range(1000)]
    shuffle(retour)
    return sorted(retour[:12])

def create_boutons():
    from random import shuffle

    boutons=[2,3,4,5,6,9,10]
    shuffle(boutons)
    return sorted(boutons[:4])


def construit_ennonce(l,b):
    chaine = "On dispose de 12 ampoules éteintes numérotées : \n"
    chaine+= str([x for x in l])
    chaine+="\n Et de 4 interrupteurs numérotés : \n"
    chaine+= str([x for x in b])
    chaine+="""\n Quand on appuie sur l'un des interrupteurs,
les ampoules dont les numéros sont multiples du nombre insiqué change d'état :
Elle passe d'éteinte à allumer ou d'allumer à éteinte..."""
    chaine+="Quelles sont les ampoules allumées après avoir actionné les 4 interrupteurs ?"
    
    print(chaine)


def construit_solutions(a):
    
def action (ampoule, bouton):
    if ampoule.nb % bouton ==0:
        ampoule.etat= ! ampoule.etat
        return ampoule
    
    
def exercice():
    
    l=create_liste()
    b=create_boutons()
    construit_ennonce(l,b)
    ampoules=[ampoule(x) for x in l]
    for i in b:
        for a in ampoules:
            action(a,i)
    construit_solutions(ampoules)



exercice()
