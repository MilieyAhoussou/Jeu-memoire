import numpy as np #système d'aléatoire #condition de victoire
import bouclejeu
rejouer = True

#Boucle de jeu
while rejouer :
    difficulte = bouclejeu.choix_difficulte()
    bouclejeu.jouer_partie(difficulte)
    rejouer_input = input("Voulez vous lancez une nouvelle partie ? oui(o)/non(n) : ").lower()
    if rejouer_input == "o":
        rejouer = True
    else :
        rejouer = False
print("Aurevoir")