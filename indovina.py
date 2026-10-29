"""Gioco "Indovina il numero" da terminale."""

import random

MINIMO = 1
MASSIMO = 100
# Comandi che si possono scrivere al posto di un numero per abbandonare
COMANDI_ABBANDONO = ("esci", "abbandona", "resa")
# Ogni quanti tentativi sbagliati il gioco propone di arrendersi
TENTATIVI_PER_RESA = 5


def confronta(tentativo, segreto):
    """Confronta il tentativo con il numero segreto.

    Restituisce "più alto" se il segreto è più grande del tentativo,
    "più basso" se è più piccolo, "giusto" se sono uguali.
    """
    if tentativo < segreto:
        return "più alto"
    if tentativo > segreto:
        return "più basso"
    return "giusto"


def e_comando_abbandono(testo):
    """True se il testo è un comando per abbandonare la partita."""
    return testo.strip().lower() in COMANDI_ABBANDONO


def leggi_numero(testo):
    """Converte il testo in un numero intero tra MINIMO e MASSIMO.

    Restituisce None se il testo non è un numero valido,
    così il gioco può chiedere di riprovare senza bloccarsi.
    """
    try:
        numero = int(testo)
    except ValueError:
        return None
    if numero < MINIMO or numero > MASSIMO:
        return None
    return numero


def aggiorna_intervallo(minimo, massimo, tentativo, risultato):
    """Restringe l'intervallo possibile dopo un tentativo sbagliato.

    Restituisce la coppia (minimo, massimo) aggiornata.
    """
    if risultato == "più alto":
        # Il segreto è maggiore del tentativo: alziamo il minimo
        minimo = max(minimo, tentativo + 1)
    elif risultato == "più basso":
        # Il segreto è minore del tentativo: abbassiamo il massimo
        massimo = min(massimo, tentativo - 1)
    return minimo, massimo


def messaggio_richiesta(facilitata, minimo, massimo):
    """Restituisce il messaggio che chiede il tentativo.

    In modalità facilitata mostra l'intervallo in cui si trova il numero.
    """
    if facilitata:
        return f"Scegli un numero (tra {minimo} e {massimo}): "
    return "Il tuo tentativo: "


def deve_proporre_resa(sbagliati):
    """True ogni TENTATIVI_PER_RESA tentativi sbagliati (5, 10, 15, ...)."""
    return sbagliati > 0 and sbagliati % TENTATIVI_PER_RESA == 0


def gioca_partita():
    """Gioca una partita completa e mostra i tentativi usati."""
    # Il computer sceglie il numero segreto (estremi inclusi)
    segreto = random.randint(MINIMO, MASSIMO)
    tentativi = 0
    sbagliati = 0

    facilitata = vuole_rigiocare(input("Attivare la modalità facilitata? (s/n) "))
    # Intervallo in cui può ancora trovarsi il numero
    minimo, massimo = MINIMO, MASSIMO

    print(f"Ho scelto un numero da {MINIMO} a {MASSIMO}. Prova a indovinarlo!")

    while True:
        testo = input(messaggio_richiesta(facilitata, minimo, massimo))
        if e_comando_abbandono(testo):
            # L'utente abbandona: riveliamo il numero e finisce la partita
            print(f"Hai abbandonato. Il numero era {segreto}.")
            break
        tentativo = leggi_numero(testo)
        if tentativo is None:
            # Input non valido: avvisiamo e non contiamo il tentativo
            print(f"Scrivi un numero intero da {MINIMO} a {MASSIMO}.")
            continue
        tentativi += 1

        risultato = confronta(tentativo, segreto)
        if risultato == "giusto":
            parola = "tentativo" if tentativi == 1 else "tentativi"
            print(f"Bravo! Hai indovinato in {tentativi} {parola}.")
            break
        print(f"Prova con un numero {risultato}.")
        minimo, massimo = aggiorna_intervallo(minimo, massimo, tentativo, risultato)

        sbagliati += 1
        if deve_proporre_resa(sbagliati):
            if vuole_rigiocare(input("Vuoi arrenderti? (s/n) ")):
                print(f"Il numero era {segreto}.")
                break


def vuole_rigiocare(risposta):
    """Restituisce True se la risposta è un sì (s, si, sì), altrimenti False."""
    return risposta.strip().lower() in ("s", "si", "sì")


def main():
    try:
        while True:
            gioca_partita()
            if not vuole_rigiocare(input("Vuoi rigiocare? (s/n) ")):
                break
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C o fine dell'input: usciamo senza mostrare errori
        print()
    print("Grazie per aver giocato, a presto!")


if __name__ == "__main__":
    main()
