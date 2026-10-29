# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stato del progetto

Repository appena inizializzato: al momento non contiene codice sorgente, test, README né file di configurazione (`pyproject.toml`, `requirements.txt`). Aggiornare questo file quando compaiono comandi di build/test/lint e una struttura da documentare.

## Regole del progetto

- Progetto: gioco "Indovina il numero" da terminale, a scopo didattico.
- Python 3.14, solo libreria standard (pytest è ammesso solo per i test).
- Codice semplice e commentato in italiano, adatto a chi impara.
- Test con pytest.
- Fare un commit dopo ogni funzionalità che funziona.

## Ambiente

- Windows con PowerShell, Python 3.14.
- Ambiente virtuale in `.venv/` (ignorato da git). Attivazione: `.\.venv\Scripts\Activate.ps1`
- Identità git configurata solo a livello di repository (non globale).
