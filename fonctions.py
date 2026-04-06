import math
import numpy as np
import random
import json
import os

data = "data.json"

def afficher_plateau(plateau):
    #Calcule dub nombre de lignes et de Colonnes pour avoir le tableau le plus carré possible
    colonne = math.ceil(math.sqrt(len(plateau)))
    ligne = math.ceil(len(plateau)/colonne)

    #remplir la place restante avec X s'il y'en a
    plateau = plateau + ["X"]*(ligne*colonne-len(plateau))

    #affichage du plateau
    print(np.array(plateau).reshape(ligne, colonne))

#cette fonction crée les paires de cartes qui devront etre trouver par le joueur
def jeu_carte(dif):
    cartes = list(range(dif//2))
    paires_cartes = cartes*2
    # cartes =[]
    # for i in range(dif//2):
    #     cartes.append("Carte_"+str(i))
    # paires_cartes = cartes*2
    random.shuffle(paires_cartes)
    return paires_cartes

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
                print("Vous avez déja choisi cette carte")
                continue
        break
    return carte

def demander_nom_joueur():
    while True :
        nom_joueur = input("entrez votre nom >")
        if nom_joueur.isalnum() :
            break
        else : 
            print("Votre pseudo ne peut contenir des espaces")
            continue
    return nom_joueur

def donnees_jeu(nom_joueur,score,difficulte):
    return {"Nom":nom_joueur, "Score": score, "Difficulté": difficulte}

def conversion_json_python(data):
    with open(data, mode="r", encoding="utf_8") as read_file:
        score_python = json.load(read_file)
    return score_python

def conversion_python_json(data,tableau):
    with open(data, mode="w", encoding="utf_8") as write_file:
        json.dump(tableau,write_file, indent = 4)

def sauvegarder(nom_joueur,score,difficulte,dataj = data):
    tableau = conversion_json_python(dataj)
    tableau.append(donnees_jeu(nom_joueur,score,difficulte))
    conversion_python_json(dataj,tableau)

# def charger_score():
#     if os.path.exists(data) :
#         return [1]
#     else :
#         return [0]