# Indovina il numero

Piccolo gioco da terminale a scopo didattico: il computer sceglie un numero
da 1 a 100 e tu cerchi di indovinarlo, con i suggerimenti "più alto" / "più basso".

Funzioni:

- **Modalità facilitata** (opzionale): mostra l'intervallo in cui si trova il numero.
- **Proposta di resa**: ogni 5 tentativi sbagliati puoi arrenderti.
- **Abbandono**: al posto di un numero scrivi `esci` (o `abbandona`, `resa`).

Richiede Python 3.14; il gioco usa solo la libreria standard.

## Installazione (Windows, PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

`requirements-dev.txt` serve solo per i test (installa pytest).

## Giocare

```powershell
python indovina.py
```

## Lanciare i test

```powershell
pytest
```
