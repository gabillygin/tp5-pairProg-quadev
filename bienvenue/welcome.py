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
                if prenom == input[-1]:
                    sortie += ' and ' + prenom
                else:
                    sortie += ', ' + prenom
    return (sortie,sortie_maj)


def sortie_bienvenue(input):
    sortie = hello_prenom(input)
    if sortie[1] != "HELLO":
        if sortie[0] != "Hello" and sortie[0] != "Hello, my friend":
            return sortie[0] + '. AND ' + sortie[1] + ' !'
        return sortie[1] + '!'
    return sortie[0]
