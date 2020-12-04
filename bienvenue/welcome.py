def supprime_prenom_non_affiche(input):
    for prenom in input:
        if prenom[0] == '!':
            for check in input:
                if prenom[1:].strip() == check.strip():
                    del input[input.index(check)]
            del input[input.index(prenom)]
    return input


def compte_occ_prenom_min_maj(input):
    nb_prenom_min = []
    nb_prenom_maj = []
    for prenom in input:
        if(prenom.isupper()):
            nb_prenom_maj.append(input.count(prenom))
            nb_prenom_min.append(0)
        else:
            nb_prenom_min.append(input.count(prenom))
            nb_prenom_maj.append(0)
        for check in input[input.index(prenom) + 1:]:
            if prenom.strip() == check.strip():
                del input[input.index(check)]
    return nb_prenom_min,nb_prenom_maj


def traitement_input(input):
    input = input.split(',')
    sortie = "Hello"
    sortie_maj = "HELLO"

    if input[0] == '':
        sortie += ', my friend'
        return sortie, sortie_maj

    input = supprime_prenom_non_affiche(input)

    if input == []:
        sortie += ', my friend'
        return sortie, sortie_maj

    nb_prenom_min, nb_prenom_maj = compte_occ_prenom_min_maj(input)

    if sum(nb_prenom_min) >= 5:
        sortie += ', world'
        print(sortie,' ',input)
        if contient_yoda(input) == 1:
            print("oui")
            sortie = sortie[7:]
            sortie = sortie.capitalize()
            sortie += ", Hello"
        return sortie, sortie_maj
    elif sum(nb_prenom_maj) >= 5:
        sortie_maj += ', WORLD'
        return sortie, sortie_maj

    for prenom in input:
        if len(prenom.strip()) == 0:
            sortie += ', my friend'
            return sortie, sortie_maj
        if prenom.isupper():
            prenom = prenom.strip()
            sortie_maj += ', ' + prenom
        else:
            if prenom == input[-1] and len(input) != 1:
                if nb_prenom_maj[input.index(prenom)] > 1:
                    prenom = prenom.strip()
                    sortie += ' and ' + prenom.capitalize()
                else:
                    prenom = prenom.strip()
                    sortie += ' and ' + prenom.capitalize()
            else:
                if nb_prenom_min[input.index(prenom)] > 1:
                    prenom = prenom.strip()
                    sortie += ', ' + prenom.capitalize() + '(x' + str(nb_prenom_min[input.index(prenom)]) + ')'
                else:
                    prenom = prenom.strip()
                    sortie += ', ' + prenom.capitalize()

    if contient_yoda(sortie)==1:
        sortie = sortie[7:]
        sortie += ", Hello"

    return [sortie, sortie_maj]


def contient_yoda(input):
    if 'yoda' in input or 'Yoda' in input:
        return 1
    return 0


def sortie_bienvenue(input):
    sortie = traitement_input(input)
    if sortie[1] != "HELLO":
        if sortie[0] != "Hello" and sortie[0] != "Hello, my friend":
            return sortie[0] + '. AND ' + sortie[1] + ' !'
        return sortie[1] + '!'
    return sortie[0]
