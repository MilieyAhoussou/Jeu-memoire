#Déclaration des variables
def afficher_plateau(plateau):
    for index, element in enumerate(plateau):
        print(f"{index}: {element}")

def jeu_carte(dif,i):
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

def verification_carte(difficulte, victoire, premiere):  
    carte_valide = False
    while carte_valide == False :
        carte = input(">")
        if carte.isdigit():
            carte = int(carte)
            carte_valide = True
        else:
            print("entrez un nombre s'il vous plait")
            continue
        if carte<0 or carte>difficulte-1:
            print("Les indices sont compris entre 0 et "+ str(difficulte-1))
            carte_valide = False
            continue
        elif carte in victoire:
            print("Vous avez déja trouvé cette paire")
            carte_valide = False
            continue

        if premiere != None:
            if carte == premiere:
                print("Vous avez déja choisi ce nombre")
                carte_valide = False
                continue
    return carte


import random,sys #système d'aléatoire
victoirejeu = False #condition de victoire
tempo = [] #
temp = []
essaies = 0 #nombre d'éssais
score = 0 #score de la partie
score_multiplier = 200
rejouer = False
#Boucle de jeu
while victoirejeu == False or rejouer == True :
    victoirejeu = False
    tempo = [] #
    temp = []
    i = 0
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
        tempo.append("X")
        temp.append("X")

    afficher_plateau(tempo)

    # print(jeu)
    print("Utilisez les indices pour choisir une carte, il y'en de 0 à "+ str(difficulte-1))
    while(len(victoire) != len(jeu)):
        tempo  = temp.copy()
        essaies += 1
        print("essai "+str(essaies))
        print("choisissez une première carte")

        premiere = None
        premiere = verification_carte(difficulte, victoire, premiere)
        

        tempo[premiere] = jeu[premiere]

        afficher_plateau(tempo)

        print("choisissez une deuxième carte")

        deuxieme = verification_carte(difficulte, victoire, premiere)

        tempo[deuxieme] = jeu[deuxieme]

        afficher_plateau(tempo)
        
        if jeu[premiere] == jeu[deuxieme]:
            victoire.append(premiere)
            victoire.append(deuxieme)
            # print(victoire)
            reste = reste-1
            print("Bravo vous avez trouvé une paire il vous reste "+ str(reste)+" paires")
            temp = tempo.copy()
            score += score_multiplier
            score_multiplier = 200
            afficher_plateau(temp)
            # print(jeu)
        else :
            print("Essayez encore")
            if score_multiplier > 50:
                score_multiplier -= 50
            tempo = temp.copy()
    victoirejeu = True
    print("Bravo vous avez gagné avec " +str(essaies)+" essaies "+"score : "+str(score))
    rejouer_input = input("Voulez vous lancez une nouvelle partie ? oui(o)/non(n) : ").lower()
    if rejouer_input == "o":
        rejouer = True
    else :
        rejouer = False
print("Aurevoir")