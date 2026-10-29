from indovina import confronta


def test_confronta_segreto_piu_alto():
    assert confronta(10, 50) == "più alto"


def test_confronta_segreto_piu_basso():
    assert confronta(90, 50) == "più basso"


def test_confronta_giusto():
    assert confronta(50, 50) == "giusto"
