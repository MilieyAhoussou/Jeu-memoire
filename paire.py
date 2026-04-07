import numpy as np #système d'aléatoire #condition de victoire
import bouclejeu
import fonctions
rejouer = True

#Boucle de jeu
while rejouer :
    print("Menu")
    print("1. Lancez une partie")
    print("2. Afficher les scores")
    print("3. Quitter")
    choix_menu = input(">")
    if choix_menu == "1":
        pseudo = fonctions.demander_nom_joueur()
        difficulte = bouclejeu.choix_difficulte()
        score = bouclejeu.menu(difficulte)
        fonctions.sauvegarder(pseudo,score,difficulte)
        rejouer = bouclejeu.demander_rejouer()
    if choix_menu == "2":
        fonctions.afficher_tableau(fonctions.conversion_json_python())
    if choix_menu == "3":
        quit()
print("Aurevoir")