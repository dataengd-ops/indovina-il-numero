from indovina import (
    aggiorna_intervallo,
    confronta,
    deve_proporre_resa,
    e_comando_abbandono,
    leggi_numero,
    messaggio_richiesta,
    vuole_rigiocare,
)


def test_vuole_rigiocare_si():
    assert vuole_rigiocare("s")
    assert vuole_rigiocare(" SI ")
    assert vuole_rigiocare("sì")


def test_vuole_rigiocare_no():
    assert not vuole_rigiocare("n")
    assert not vuole_rigiocare("")
    assert not vuole_rigiocare("forse")


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


def test_aggiorna_intervallo_esempio():
    # "più basso di 57" poi "più alto di 29" -> tra 30 e 56
    minimo, massimo = aggiorna_intervallo(1, 100, 57, "più basso")
    minimo, massimo = aggiorna_intervallo(minimo, massimo, 29, "più alto")
    assert (minimo, massimo) == (30, 56)


def test_aggiorna_intervallo_non_si_allarga():
    # Un tentativo fuori dall'intervallo attuale non deve allargarlo
    assert aggiorna_intervallo(30, 56, 10, "più alto") == (30, 56)
    assert aggiorna_intervallo(30, 56, 90, "più basso") == (30, 56)


def test_messaggio_richiesta():
    assert messaggio_richiesta(True, 30, 56) == "Scegli un numero (tra 30 e 56): "
    assert messaggio_richiesta(False, 30, 56) == "Il tuo tentativo: "


def test_deve_proporre_resa():
    assert not deve_proporre_resa(0)
    assert not deve_proporre_resa(4)
    assert deve_proporre_resa(5)
    assert not deve_proporre_resa(6)
    assert deve_proporre_resa(10)


def test_comando_abbandono():
    assert e_comando_abbandono("esci")
    assert e_comando_abbandono("  ESCI ")
    assert not e_comando_abbandono("42")
    assert not e_comando_abbandono("")
