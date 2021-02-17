# revISEE
Other languages: [English](README.md), [Italiano](README.it.md)

Calcola il saldo medio giornaliero e il saldo a fine anno per il tuo conto Revolut. 
L'implementazione segue l'algoritmo descritto [qui](https://www.agenziaentrate.gov.it/portale/it/web/guest/schede/comunicazioni/integrativa-archivio-dei-rapporti-con-operatori-finanziari/giacenza-media-annua).

Il saldo medio giornaliero per i conti in valuta estera è convertito in EUR su base giornaliera usando il tasso di conversione giornaliero.
Poiché l'API per recuperare i valori forex storici è piuttosto lenta, lasciate il tempo all'algoritmo di eseguire. 
Attivare la modalità verbose per seguire lo stato.

Per qualsiasi suggerimento o problema, apri un nuovo issue o contribuisci direttamente con una pull-request.

## How to
Inizia creando un nuovo ambiente python 3.8. Se non hai familiarità con python, ti suggerisco di usare [Anaconda](https://www.anaconda.com/products/individual#Downloads).

Apri un terminale e installa le dipendenze richieste usando il file `requirements.txt` (apri i'Anaconda Prompt se stai usando Windows).

```
>> pip install -r /path/to/requirements.txt
```

Raccogli tutti gli estratti conto per le diverse valute in formato Excel in un'unica cartella e assicurati che:
* coprano il periodo per cui vuoi effettuare i calcoli (possono anche coprire un periodo più lungo),
* non siano stati rinominati - dovrebbero assomigliare a: `Revolut-[CUR]-*.csv`.

Scarica l'ultima [release](https://github.com/pietropelizzari/revISEE/releases/latest) e scompattala. 
Ora puoi copiare lo script `revISEE.py` nella cartella contenente le dichiarazioni, oppure puoi usare l'opzione path `-p` in fase di esecuzione.

Raggiungi la cartella contenente lo script con il tuo terminale ed eseguilo con le opzioni necessarie. 
Ricordati di impostare i separatori decimali e delle migliaia corretti a seconda della lingua impostata sul tuo telefono.

Il comando avrà un aspetto simile a questo:

```
>>> python revISEE.py -p "C:-Users\name\Documents\Revolut" -y 2019 --decsep , --thosep .
```

Dipendenze:
* [forex-python](https://pypi.org/project/forex-python/)
* [dateparser](https://pypi.org/project/dateparser/)
* pandas
* numpy

## Aiuto

```
uso: python revISEE.py [opzioni]

Calcola i valori richiesti per l'ISEE italiano a partire dagli estratti conto di Revolut

argomenti opzionali:
  -h, --help            mostra questo messaggio di aiuto e esce
  -p PATH, --path PATH  percorso della cartella contenente gli estratti conto - predefinito: cwd
  -y YEAR, --year YEAR  anno per il calcolo - predefinito: 2 anni fa
  -c CURR, --curr CURR  valuta di destinazione - predefinito: EUR
  --decsep DECSEP       separatore decimale - predefinito: .
  --thosep THOSEP       separatore delle migliaia - predefinito: ,
  --logging LOGGING     imposta il livello di logging: 10 (DEBUG), 20 (INFO), 30 (WARNING) - predefinito: 30 (WARNING)
  --detailed            stampa i saldi per ogni valuta

Licenza MIT - Copyright (c) 2021 Pietro Pelizzari



usage: python revISEE.py [options]

Compute values required for italian ISEE from Revolut statements

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to statements folder - default: cwd
  -y YEAR, --year YEAR  year for computation - default: 2 years ago
  -c CURR, --curr CURR  target currency - default: EUR
  --decsep DECSEP       decimal separator - default: .
  --thosep THOSEP       thousands separator - default: ,
  --detailed            print balances for each currency
  -v VERB, --verb VERB  set logging level: 10 (DEBUG), 20 (INFO), 30 (WARNING) - default: 30 (WARNING)

MIT License - Copyright (c) 2021 Pietro Pelizzari
```

## Disclaimer

**revISEE** non è in alcun modo garantito o supportato da Revolut.