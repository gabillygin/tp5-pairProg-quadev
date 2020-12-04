def test_sortie_bienvenue_normal():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel') == "Hello, Gabriel"
    assert hp('   ') == 'Hello, my friend'
    assert hp('gabriel  , Nicolas  ') == "Hello, Gabriel and Nicolas"


def test_sortie_bienvenue_empty():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('   ') == 'Hello, my friend'
    assert hp('') == 'Hello, my friend'


def test_sortie_bienvenue_maj():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('NICOLAS') == "HELLO, NICOLAS!"


def test_sortie_bienvenue_normal_maj():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,NICOLAS') == "Hello, Gabriel. AND HELLO, NICOLAS !"
    #ISSUE / ! \
    #assert hp('gabriel, nicolas,NICOLAS') == "Hello, Gabriel, Nicolas. AND HELLO, NICOLAS !"

def test_sortie_bienvenue_and():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,Nicolas') == "Hello, Gabriel and Nicolas"

def test_sortie_bienvenue_non_affiche():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('!gabriel, gabriel, nicolas') == "Hello, Nicolas"
    assert hp('!gabriel,gabriel') == "Hello, my friend"
    assert hp('!gabriel') == "Hello, my friend"


def test_sortie_bienvenue_multiple():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,gabriel') == "Hello, Gabriel(x2)"


def test_sortie_bienvenue_world_min():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,tony,denis,france,nina,robinson') == "Hello, world"


def test_sortie_bienvenue_world_maj():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('GABRIEL,TONY,DENIS,FRANCE,NONE,ROBINSON') == "HELLO, WORLD!"


def test_sortie_bienvenue_yoda():
    from bienvenue.welcome import sortie_bienvenue as hp
    assert hp('gabriel,yoda') == "Gabriel and Yoda, Hello"
    assert hp('yoda') == "Yoda, Hello"
    assert hp('yoda,gabriel,nicolas,denis,françouise,papy') == "World, Hello"

