from indovina import confronta, leggi_numero


def test_leggi_numero_valido():
    assert leggi_numero("42") == 42
    assert leggi_numero("  7 ") == 7


def test_leggi_numero_non_numerico():
    assert leggi_numero("ciao") is None
    assert leggi_numero("") is None
    assert leggi_numero("3.5") is None


def test_leggi_numero_fuori_intervallo():
    assert leggi_numero("0") is None
    assert leggi_numero("101") is None


def test_confronta_segreto_piu_alto():
    assert confronta(10, 50) == "più alto"


def test_confronta_segreto_piu_basso():
    assert confronta(90, 50) == "più basso"


def test_confronta_giusto():
    assert confronta(50, 50) == "giusto"
