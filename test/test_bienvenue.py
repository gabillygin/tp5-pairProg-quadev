def test_hello_prenom_normal():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel') == "Hello, Gabriel"
    assert hp('   ') == 'Hello, my friend'
    assert hp('') == 'Hello, my friend'


def test_hello_prenom_empty():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('   ') == 'Hello, my friend'
    assert hp('') == 'Hello, my friend'


def test_hello_prenom_maj():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('NICOLAS') == "HELLO, NICOLAS!"


def test_hello_prenom_normal_maj():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,NICOLAS') == "Hello, Gabriel. AND HELLO, NICOLAS !"
    #ISSUE / ! \
    #assert hp('gabriel, nicolas,NICOLAS') == "Hello, Gabriel, Nicolas. AND HELLO, NICOLAS !"

def test_hello_prenom_and():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,Nicolas') == "Hello, Gabriel and Nicolas"