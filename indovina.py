"""Gioco "Indovina il numero" da terminale."""

import random

MINIMO = 1
MASSIMO = 100


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


def gioca_partita():
    """Gioca una partita completa e mostra i tentativi usati."""
    # Il computer sceglie il numero segreto (estremi inclusi)
    segreto = random.randint(MINIMO, MASSIMO)
    tentativi = 0

    print(f"Ho scelto un numero da {MINIMO} a {MASSIMO}. Prova a indovinarlo!")

    while True:
        tentativo = leggi_numero(input("Il tuo tentativo: "))
        if tentativo is None:
            # Input non valido: avvisiamo e non contiamo il tentativo
            print(f"Scrivi un numero intero da {MINIMO} a {MASSIMO}.")
            continue
        tentativi += 1

        risultato = confronta(tentativo, segreto)
        if risultato == "giusto":
            print(f"Bravo! Hai indovinato in {tentativi} tentativi.")
            break
        print(f"Prova con un numero {risultato}.")


def main():
    gioca_partita()


if __name__ == "__main__":
    main()
