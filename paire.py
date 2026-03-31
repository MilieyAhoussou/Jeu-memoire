import numpy as np #système d'aléatoire #condition de victoire
import bouclejeu
import fonctions
rejouer = True

#Boucle de jeu
while rejouer :
    pseudo = fonctions.demander_nom_joueur()
    difficulte = bouclejeu.choix_difficulte()
    score = bouclejeu.jouer_partie(difficulte)
    print(fonctions.donnees_jeu(pseudo,score,difficulte))
    rejouer = bouclejeu.demander_rejouer()
    
print("Aurevoir")