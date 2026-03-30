import numpy as np #système d'aléatoire #condition de victoire
import bouclejeu
rejouer = True

#Boucle de jeu
while rejouer :
    difficulte = bouclejeu.choix_difficulte()
    bouclejeu.jouer_partie(difficulte)
    rejouer = bouclejeu.demander_rejouer()
print("Aurevoir")