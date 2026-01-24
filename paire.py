import random,sys
victoirejeu = False
tempo = []
temp = []
essaies = 0
while victoirejeu == False :
    i = 0
    jeu = []
    victoire =[]
    print("Combien de carte voulez vous ? (choisissez un nombre paire)")
    difficulte = input(">") 
    if difficulte.isdigit(): #isdigit() permet de vérifier si une chaine de charactère est un nombre
        difficulte = int(difficulte)
    else:
        print("entrez un nombre s'il vous plait")
        continue
    if difficulte <= 1:
        print("entrez un nombre supérieur à 1 s'il vous plait")
        continue
    reste = difficulte//2
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
        if premiere.isdigit():
            premiere = int(premiere)
        else:
            print("entrez un nombre s'il vous plait")
            continue
        if premiere<0 or premiere>difficulte-1:
            print("Les indices sont compris entre 0 et "+ str(difficulte-1))
            continue
        elif premiere in victoire:
            print("Vous avez déja trouvé cette paire")
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
            for index, element in enumerate(temp):
                print(f"{index}: {element}")
            # print(jeu)
        else :
            print("Essayez encore")
            tempo = temp.copy()
    victoirejeu = True
print("Bravo vous avez gagné avec " +str(essaies)+" essaies")