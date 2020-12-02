def test_hello_prenom():
    from bienvenue.welcome import hello_prenom as hp
    assert hp('gabriel') == "Hello, Gabriel"
    assert hp('   ') == 'Hello, my friend'
    assert hp('') == 'Hello, my friend'
    assert hp('NICOLAS') == "HELLO, NICOLAS!"
    assert hp('gabriel,Nicolas') == "Hello, Gabriel, Nicolas"
    assert hp('gabriel,NICOLAS') == "Hello, Gabriel. AND HELLO, NICOLAS !"