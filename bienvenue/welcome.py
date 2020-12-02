def hello_prenom(input):
    input = input.split(',')
    sortie = "Hello"
    sortie_maj = "HELLO"
    for prenom in input:
        if len(prenom.strip()) == 0:
            prenom = "my friend"
            sortie += ', ' + prenom
        else:
            if prenom.isupper():
                sortie_maj += ', ' + prenom
            else:
                prenom = prenom.capitalize()
                sortie += ', ' + prenom

    if sortie_maj != "HELLO":
        if sortie != "Hello" and sortie != "Hello, my friend":
            return sortie + '. AND ' + sortie_maj + ' !'
        return sortie_maj + '!'
    return sortie
