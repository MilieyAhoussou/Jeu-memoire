#Déclaration des variables

import random,sys #système d'aléatoire
victoirejeu = False #condition de victoire
tempo = [] #
temp = []
essaies = 0 #nombre d'éssais
score = 0 #score de la partie
score_multiplier = 200

#Boucle de jeu
while victoirejeu == False :
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

    while i < difficulte//2:
        nombre = random.randint(1,20)
        if nombre in jeu:
            continue
        jeu.append(nombre)
        jeu.append(nombre)
        i += 1

    random.shuffle(jeu)
    for i in range(0,difficulte):
        tempo.append("X")
        temp.append("X")

    for index, element in enumerate(tempo):
        print(f"{index}: {element}")

    # print(jeu)
    print("Utilisez les indices pour choisir une carte, il y'en de 0 à "+ str(difficulte-1))
    while(len(victoire) != len(jeu)):
        essaies += 1
        print("essai "+str(essaies))
        print("choisissez une première carte")
        
        premiere = input(">")
        #vérifier si c'est un nombre
        if premiere.isdigit():
            premiere = int(premiere)
        else:
            print("entrez un nombre s'il vous plait")
            continue

        #vérification de la plage entrée
        if premiere<0 or premiere>difficulte-1:
            print("Les indices sont compris entre 0 et "+ str(difficulte-1))
            continue

        elif premiere in victoire:
            print("Vous avez déja trouvé cette paire")
            essaies -= 1
            continue
        
        tempo[premiere] = jeu[premiere]

        for index, element in enumerate(tempo):
            print(f"{index}: {element}")

        print("choisissez une deuxième carte")
        deuxieme = input(">")
        if deuxieme.isdigit():
            deuxieme = int(deuxieme)
        else:
            print("entrez un nombre s'il vous plait")
            continue
        if deuxieme<0 or deuxieme>difficulte-1:
            print("Les indices sont compris entre 0 et "+ str(difficulte-1))
            continue
        elif deuxieme in victoire:
            print("Vous avez déja trouvé cette paire")
            essaies -= 1
            continue
        elif deuxieme == premiere:
            print("Vous avez déja choisi ce nombre")
            continue

        tempo[deuxieme] = jeu[deuxieme]

        for index, element in enumerate(tempo):
            print(f"{index}: {element}")
        
        if jeu[premiere] == jeu[deuxieme]:
            victoire.append(premiere)
            victoire.append(deuxieme)
            # print(victoire)
            reste = reste-1
            print("Bravo vous avez trouvé une paire il vous reste "+ str(reste)+" paires")
            temp = tempo.copy()
            score += score_multiplier
            score_multiplier = 200
            for index, element in enumerate(temp):
                print(f"{index}: {element}")
            # print(jeu)
        else :
            print("Essayez encore")
            if score_multiplier > 50:
                score_multiplier -= 50
            tempo = temp.copy()
    victoirejeu = True
print("Bravo vous avez gagné avec " +str(essaies)+" essaies "+"score : "+str(score))