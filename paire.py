#Déclaration des variables
def afficher_plateau(plateau):
    for index, element in enumerate(plateau):
        print(f"{index}: {element}")

def jeu_carte(dif):
    i = 0
    jeu = []
    while i < dif//2:
        nombre = random.randint(1,20)
        if nombre in jeu:
            continue
        jeu.append(nombre)
        jeu.append(nombre)
        i += 1
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


import random,sys #système d'aléatoire
victoirejeu = False #condition de victoire
paires_trouvé_jeu = [] #
paires_trouvé = []
essaies = 0 #nombre d'éssais
score = 0 #score de la partie
score_multiplier = 200
rejouer = False
#Boucle de jeu
while victoirejeu == False or rejouer == True :
    victoirejeu = False
    paires_trouvé_jeu = [] #
    paires_trouvé = []
    jeu = [] #liste de cartes
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

    jeu = jeu_carte(difficulte,i)

    random.shuffle(jeu)
    for i in range(0,difficulte):
        paires_trouvé_jeu.append("X")
        paires_trouvé.append("X")

    afficher_plateau(paires_trouvé_jeu)

    # print(jeu)
    print("Utilisez les indices pour choisir une carte, il y'en de 0 à "+ str(difficulte-1))
    while(len(victoire) != len(jeu)):
        paires_trouvé_jeu  = paires_trouvé.copy()
        essaies += 1
        print("essai "+str(essaies))
        print("choisissez une première carte")

        premiere = verification_carte(difficulte, victoire)
        
        paires_trouvé_jeu[premiere] = jeu[premiere]

        afficher_plateau(paires_trouvé_jeu)

        print("choisissez une deuxième carte")

        deuxieme = verification_carte(difficulte, victoire, premiere)

        paires_trouvé_jeu[deuxieme] = jeu[deuxieme]

        afficher_plateau(paires_trouvé_jeu)
        
        if jeu[premiere] == jeu[deuxieme]:
            victoire.append(premiere)
            victoire.append(deuxieme)
            # print(victoire)
            reste = reste-1
            print("Bravo vous avez trouvé une paire il vous reste "+ str(reste)+" paires")
            paires_trouvé = paires_trouvé_jeu.copy()
            score += score_multiplier
            score_multiplier = 200
            afficher_plateau(paires_trouvé)
            # print(jeu)
        else :
            print("Essayez encore")
            if score_multiplier > 50:
                score_multiplier -= 50
            paires_trouvé_jeu = paires_trouvé.copy()
    victoirejeu = True
    print("Bravo vous avez gagné avec " +str(essaies)+" essaies "+"score : "+str(score))
    rejouer_input = input("Voulez vous lancez une nouvelle partie ? oui(o)/non(n) : ").lower()
    if rejouer_input == "o":
        rejouer = True
    else :
        rejouer = False
print("Aurevoir")