# Missione Cosmo · Il laboratorio di Berke

Un laboratorio di astronomia in italiano, recuperato dal progetto originale di Berke e preparato per GitHub Pages.

**Sito:** https://erenilturco.github.io/berke-astronomi-testi/

- Moto di rivoluzione e rotazione dei pianeti.
- Le tre leggi di Keplero riunite nella stessa sezione, con schemi e controlli interattivi.
- 18 esercizi di Keplero e 24 domande di verifica con correzioni specifiche per ogni risposta sbagliata.
- Struttura e attività del Sole, cinque schede illustrate e PDF scaricabile.
- Nessun voto, punteggio finale o classifica. Possibilità di riprovare e ripassare gli errori.
- Interfaccia responsive, navigazione da tastiera e spiegazioni annunciate alle tecnologie assistive.
- Nessun account, tracciamento o invio delle risposte; lo stato resta nella pagina e si azzera ricaricandola.

## Pubblicazione

GitHub Pages → Deploy from a branch → `main` → `/ (root)`.
Le pagine pubblicate sono già incluse nel repository: non servono Node.js o dipendenze.

## Modifiche

Modifica i file in `src/`, poi esegui `python3 build.py` e salva anche le due pagine HTML rigenerate in un commit.
Anteprima: `python3 -m http.server 8765`, poi apri http://localhost:8765.
La versione `missione-cosmo-offline.html` incorpora le schede e il PDF e funziona anche senza connessione.

## Verifica scientifica

Controllo del 31 ottobre 2026 sulle fonti NASA:

- [Orbits and Kepler’s Laws](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/)
- [Sun: Facts](https://science.nasa.gov/sun/facts/)

La prima legge pone il Sole in un fuoco dell’ellisse; la seconda riguarda aree uguali in tempi uguali. La terza usa il semiasse maggiore `a`, non la distanza istantanea: `T² = k·a³`. Nel modello solare con anni e UA si usa `T² ≈ a³`, trascurando le masse dei pianeti e le perturbazioni. Con `a = 9,5 UA`, il risultato didattico per Saturno è circa 29,3 anni e dipende dal dato arrotondato.

La fusione produce energia nel nucleo; radiazione e convezione la trasportano. La fotosfera è la superficie visibile, non solida, e lo strato più basso dell’atmosfera. La regione di transizione tra cromosfera e corona è segnalata nel testo ma omessa nello schema didattico a sei strati. Le macchie sono regioni più fredde e magnetiche; il vento solare proviene dalla corona.

Le schede sono rielaborazioni didattiche originali del materiale di studio preesistente. Il PDF scolastico originale citato nel testo non è incluso. Gli schemi non sono in scala.
