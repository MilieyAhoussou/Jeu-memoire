import fonctions
def choix_difficulte():
    while True :
        print("Combien de carte voulez vous ? (choisissez un nombre paire)")
        difficulte = input(">") 
        if difficulte.isdigit(): #isdigit() permet de vérifier si une chaine de charactère est un nombre
            difficulte = int(difficulte)
        else:
            print("entrez un nombre s'il vous plait")
            continue #reviens au début de la boucle
        if difficulte <= 1 or difficulte%2 != 0:
            print("entrez un nombre supérieur à 1 et paire s'il vous plait")
            continue 
        break
    return difficulte

def jouer_partie(difficulte) :
    essaies = 0 #nombre d'éssais
    score = 0 #score de la partie
    score_multiplier = 200
    plateau_etat_manche = [] #
    plateau_paires_trouve = []
    victoire =[]#vérification de victoire
#reviens au début de la boucle

    reste = difficulte//2 #nombre de paire restante

    jeu = fonctions.jeu_carte(difficulte)

    plateau_etat_manche = ["X"]*difficulte
    plateau_paires_trouve = ["X"]*difficulte
    
    fonctions.afficher_plateau(plateau_etat_manche)

    # print(jeu)
    print("Utilisez les indices pour choisir une carte, il y'en de 0 à "+ str(difficulte-1))
    while(reste > 0):
        plateau_etat_manche  = plateau_paires_trouve.copy()
        essaies += 1
        print("essai "+str(essaies))
        print("choisissez une première carte")

        premiere = fonctions.verification_carte(difficulte, victoire)
        
        plateau_etat_manche[premiere] = jeu[premiere]

        fonctions.afficher_plateau(plateau_etat_manche)

        print("choisissez une deuxième carte")

        deuxieme = fonctions.verification_carte(difficulte, victoire, premiere)

        plateau_etat_manche[deuxieme] = jeu[deuxieme]

        fonctions.afficher_plateau(plateau_etat_manche)
        
        if jeu[premiere] == jeu[deuxieme]:
            victoire.append(premiere)
            victoire.append(deuxieme)
            # print(victoire)
            reste = reste-1
            print("Bravo vous avez trouvé une paire il vous reste "+ str(reste)+" paires")
            plateau_paires_trouve = plateau_etat_manche.copy()
            score += score_multiplier
            score_multiplier = 200
            fonctions.afficher_plateau(plateau_paires_trouve)
            # print(jeu)
        else :
            print("Essayez encore")
            if score_multiplier > 50:
                score_multiplier -= 50
            plateau_etat_manche = plateau_paires_trouve.copy()

    print("Bravo vous avez gagné avec " +str(essaies)+" essaies "+"score : "+str(score))
    return(score)

def demander_rejouer():
    while True :
        rejouer = input("Voulez vous lancez une nouvelle partie ? oui(o)/non(n) : ").lower()
        if rejouer == "o" :
            rejouer = True
            break
        elif rejouer == "n" :
            rejouer = False
            break
        else :
            print("Cette entrée n'est pas valide entrez 'o' pour 'oui' ou 'n' pour 'non'")
    return rejouer