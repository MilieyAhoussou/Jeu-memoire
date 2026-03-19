#Déclaration des variables

def afficher_plateau(plateau):
    #Calcule dub nombre de lignes et de Colonnes pour avoir le tableau le plus carré possible
    colonne = math.ceil(math.sqrt(len(plateau)))
    ligne = math.ceil(len(plateau)/colonne)

    #remplir la place restante avec X s'il y'en a
    plateau = plateau + ["X"]*(ligne*colonne-len(plateau))

    #affichage du plateau
    print(np.array(plateau).reshape(ligne, colonne))


def jeu_carte(dif):
    i = 0
    jeu = random.sample(range(200),dif//2)
    jeu = jeu + jeu
    random.shuffle(jeu)
    return jeu

#ici premiere est certe un parametre mais pas un parametre exigé. cela veut dire que si le paramètre
#n'est pas spécifié a l'appel de la fonction dans le code, alors celle-ci prendra automatiquement la valeur qu'on lui a attribué au départ
def verification_carte(difficulte, victoire, premiere = None):  
    while True :
        carte = input(">")
        if carte.isdigit():
            carte = int(carte)
        else:
            print("entrez un nombre s'il vous plait")
            continue
        if carte<0 or carte>difficulte-1:
            print("Les indices sont compris entre 0 et "+ str(difficulte-1))
            continue
        elif carte in victoire:
            print("Vous avez déja trouvé cette paire")
            continue

        if premiere is not None:
            if carte == premiere:
                print("Vous avez déja choisi ce nombre")
                continue
        break
    return carte

import math
import numpy as np
import random,sys #système d'aléatoire
victoirejeu = False #condition de victoire
rejouer = False

#Boucle de jeu
while victoirejeu == False or rejouer == True :
    essaies = 0 #nombre d'éssais
    score = 0 #score de la partie
    score_multiplier = 200
    victoirejeu = False
    plateau_etat_manche = [] #
    plateau_paires_trouve = []
    victoire =[]#vérification de victoire
    print("Combien de carte voulez vous ? (choisissez un nombre paire)")
    difficulte = input(">") 
    if difficulte.isdigit(): #isdigit() permet de vérifier si une chaine de charactère est un nombre
        difficulte = int(difficulte)
    else:
        print("entrez un nombre s'il vous plait")
        continue #reviens au début de la boucle
    if difficulte <= 1 or difficulte%2 != 0:
        print("entrez un nombre supérieur à 1 et paire s'il vous plait")
        continue #reviens au début de la boucle
    reste = difficulte//2 #nombre de paire restante

    jeu = jeu_carte(difficulte)

    plateau_etat_manche = ["X"]*difficulte
    plateau_paires_trouve = ["X"]*difficulte
    
    afficher_plateau(plateau_etat_manche)

    # print(jeu)
    print("Utilisez les indices pour choisir une carte, il y'en de 0 à "+ str(difficulte-1))
    while(len(victoire) != len(jeu)):
        plateau_etat_manche  = plateau_paires_trouve.copy()
        essaies += 1
        print("essai "+str(essaies))
        print("choisissez une première carte")

        premiere = verification_carte(difficulte, victoire)
        
        plateau_etat_manche[premiere] = jeu[premiere]

        afficher_plateau(plateau_etat_manche)

        print("choisissez une deuxième carte")

        deuxieme = verification_carte(difficulte, victoire, premiere)

        plateau_etat_manche[deuxieme] = jeu[deuxieme]

        afficher_plateau(plateau_etat_manche)
        
        if jeu[premiere] == jeu[deuxieme]:
            victoire.append(premiere)
            victoire.append(deuxieme)
            # print(victoire)
            reste = reste-1
            print("Bravo vous avez trouvé une paire il vous reste "+ str(reste)+" paires")
            plateau_paires_trouve = plateau_etat_manche.copy()
            score += score_multiplier
            score_multiplier = 200
            afficher_plateau(plateau_paires_trouve)
            # print(jeu)
        else :
            print("Essayez encore")
            if score_multiplier > 50:
                score_multiplier -= 50
            plateau_etat_manche = plateau_paires_trouve.copy()
    victoirejeu = True
    print("Bravo vous avez gagné avec " +str(essaies)+" essaies "+"score : "+str(score))
    rejouer_input = input("Voulez vous lancez une nouvelle partie ? oui(o)/non(n) : ").lower()
    if rejouer_input == "o":
        rejouer = True
    else :
        rejouer = False
print("Aurevoir")